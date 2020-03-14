#!/usr/bin/env python
"""
    Test Demos Python Script: regression test of DOOM demos in Eternity
    Copyright (C) 2020  Ioan Chera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
import multiprocessing
import os
import re
import subprocess
import sys
import time
from joblib import Parallel, delayed
from scripts import notifications

# set the base args (common to all games)
ARGS_BASE = ['eternity-port/eternity', '-base', 'eternity-port/base', '-user', 'eternity-port/user',
             '-nodraw', '-nosound']
ARGS_DOOM = ['-iwad', 'DOOM.WAD']
ARGS_DOOM2 = ['-iwad', 'DOOM2.WAD']
ARGS_PLUTONIA = ['-iwad', 'PLUTONIA.WAD']

ARGS_MAPPING = {
    '1': ARGS_DOOM,
    '2': ARGS_DOOM2,
    'p': ARGS_PLUTONIA
}

###################################################################
###################################################################

# https://stackoverflow.com/a/5967539
# "How to correctly sort a string with a number inside? [duplicate]"


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]

###################################################################
###################################################################


def call_eternity(a):
    with open(os.devnull, 'w') as black_hole:
        subprocess.call(a, stdout=black_hole)
        sys.stdout.write('.')
        sys.stdout.flush()


def run_program(command_line_args):
    # 0. Get data from .data
    with open('demo-list.data', 'r') as demo_list:
        demo_list_lines = demo_list.readlines()
    scenarios = []
    for line in demo_list_lines:
        scenario = line.split()
        if len(scenario) < 2:
            continue
        scenarios.append(scenario)

    # now we have the items

    # delete old entries
    temp_file_list = [os.path.join('temp-logs', f) for f in os.listdir("temp-logs") if f.endswith(".txt")]
    for f in temp_file_list:
        os.remove(f)

    # iterate the table entries
    index = 0
    commands_list = []

    for scenario in scenarios:
        arguments = list(ARGS_BASE)
        extra_args = ARGS_MAPPING.get(scenario[0])
        if not extra_args:
            print('Unknown game type', scenario[0])
            continue
        if command_line_args.folders and scenario[1] not in command_line_args.folders:
            continue

        arguments.extend(extra_args)
        if len(scenario) > 2:
            arguments.extend(scenario[2:])
        # now look in the folder with demos
        files = sorted(os.listdir(scenario[1]))
        for f in files:
            if f.lower().endswith('.lmp'):
                demo_path = os.path.join(scenario[1], f)
                args_complete = list(arguments)
                args_complete.extend(['-fastdemo', demo_path])
                temp_log_path = os.path.join('temp-logs', str(index) + '.txt')
                args_complete.extend(['-demolog', temp_log_path])
                commands_list.append(args_complete)
                index += 1

    # now we have the commands list. print it
    max_cpu_count = multiprocessing.cpu_count()
    cpu_count = int(command_line_args.cpu_count) if command_line_args.cpu_count else max_cpu_count
    cpu_count = max(1, min(cpu_count, max_cpu_count))
    print(f'Using {cpu_count} of {max_cpu_count} ({cpu_count / max_cpu_count * 100}) processor cores.')

    # Decide CPU count now

    print('Testing', len(commands_list), 'demos.')

    time_start = time.time()

    Parallel(n_jobs=cpu_count)(delayed(call_eternity)(a) for a in commands_list)

    time_end = time.time()
    time_elapsed = time_end - time_start

    print()
    print('Elapsed time:', time_elapsed)
    if commands_list:
        print('Average per demo:', time_elapsed / len(commands_list))

    temp_file_list = [os.path.join('temp-logs', f) for f in sorted(os.listdir("temp-logs"), key=natural_keys) if
                      f.endswith(".txt")]

    try:
        os.remove('demolog.txt')
    except OSError:
        pass

    with open('demolog.txt', 'w') as outfile:
        for f in temp_file_list:
            with open(f) as infile:
                outfile.write(infile.read())
            os.remove(f)

    notifications.show('Demo testing done!')


if __name__ == "__main__":
    print("Test Demos  Copyright (C) 2020  Ioan Chera\n",
          "This program comes with ABSOLUTELY NO WARRANTY.\n",
          "This is free software, and you are welcome to redistribute it\n",
          "under certain conditions. For details read COPYING-testdemos.txt.")
    parser = argparse.ArgumentParser(description='Execute demos for Eternity in a batch.')
    parser.add_argument('--cpu', dest='cpu_count', help='Set the number of CPUs to do the job (default: all of them)')
    parser.add_argument('folders', metavar='folder', nargs='*', help='optional list of folder names to filter in')
    args = parser.parse_args()
    run_program(args)
