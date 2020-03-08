#!/usr/bin/env python
import multiprocessing
import os
import subprocess
import re
import sys
import time
from joblib import Parallel, delayed

# set the base args (common to all games)
ARGS_BASE = ['eternity-port/eternity', '-base', 'eternity-port/base', '-user', 'eternity-port/user',
             '-nodraw', '-nosound']
ARGS_DOOM = ['-iwad', 'DOOM.WAD']
ARGS_DOOM2 = ['-iwad', 'DOOM2.WAD']

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


def run_program():
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
        args = list(ARGS_BASE)
        if scenario[0] == '1':
            args.extend(ARGS_DOOM)
        elif scenario[0] == '2':
            args.extend(ARGS_DOOM2)
        else:
            continue
        if len(scenario) > 2:
            args.extend(scenario[2:])
        # now look in the folder with demos
        files = sorted(os.listdir(scenario[1]))
        for f in files:
            if f.lower().endswith('.lmp'):
                demo_path = os.path.join(scenario[1], f)
                args_complete = list(args)
                args_complete.extend(['-fastdemo', demo_path])
                temp_log_path = os.path.join('temp-logs', str(index) + '.txt')
                args_complete.extend(['-demolog', temp_log_path])
                commands_list.append(args_complete)
                index += 1

    # now we have the commands list. print it
    cpu_count = multiprocessing.cpu_count()

    print('Testing', len(commands_list), 'demos.')

    time_start = time.time()

    Parallel(n_jobs=cpu_count)(delayed(call_eternity)(a) for a in commands_list)

    time_end = time.time()
    time_elapsed = time_end - time_start

    print()

    print('Elapsed time:', time_elapsed, '; average per demo: ', time_elapsed / len(commands_list))

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

    subprocess.call(['osascript', '-e', 'display notification "Demo testing done!" with title "Eternity demo test"'])


if __name__ == "__main__":
    run_program()
