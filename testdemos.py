#!/usr/bin/env python
import multiprocessing
import os
import subprocess
import sys
import time
from joblib import Parallel, delayed

###################################################################
###################################################################

# https://stackoverflow.com/a/5967539
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

###################################################################
###################################################################


# 0. Get data from .data
with open('demo-list.data', 'r') as demolist:
    s = demolist.readlines()
items = []
for l in s:
    item = l.split()
    if len(item) < 2:
        continue
    items.append(item)

# now we have the items
# set the base args (common to all games)
args_base = ['eternity-port/eternity', '-base', 'eternity-port/base', '-user', 'eternity-port/user', '-nodraw', '-nosound']
args_doom = ['-iwad', 'DOOM.WAD']
args_doom2 = ['-iwad', 'DOOM2.WAD']


# delete old entries
filelist = [ os.path.join('temp-logs', f) for f in os.listdir("temp-logs") if f.endswith(".txt") ]
for f in filelist:
    os.remove(f)

# iterate the table entries
index = 0
commands_list = []
for item in items:
    args = list(args_base)
    if item[0] == '1':
        args.extend(args_doom)
    elif item[0] == '2':
        args.extend(args_doom2)
    else:
        continue
    if len(item) > 2:
        args.extend(item[2:])
    # now look in the folder with demos
    files = sorted(os.listdir(item[1]))
    for f in files:
        if f.lower().endswith('.lmp'):
            demo_path = os.path.join(item[1], f)
            args_complete = list(args)
            args_complete.extend(['-fastdemo', demo_path])
            temp_log_path = os.path.join('temp-logs', str(index) + '.txt')
            args_complete.extend(['-demolog', temp_log_path])
            commands_list.append(args_complete)
            index += 1

# now we have the commands list. print it
cpu_count = multiprocessing.cpu_count()

print 'Testing', len(commands_list), 'demos.'

black_hole = open(os.devnull, 'w')

def call_eternity(a):
    subprocess.call(a, stdout=black_hole)
    sys.stdout.write('.')
    sys.stdout.flush()
    
time_start = time.time()

Parallel(n_jobs=cpu_count)(delayed(call_eternity)(a) for a in commands_list)

time_end = time.time()
time_elapsed = time_end - time_start

print

print 'Elapsed time:', time_elapsed, '; average per demo: ', time_elapsed / len(commands_list)

filelist = [ os.path.join('temp-logs', f) for f in sorted(os.listdir("temp-logs"), key=natural_keys) if f.endswith(".txt") ]

try:
    os.remove('demolog.txt')
except OSError:
    pass
    
with open('demolog.txt', 'w') as outfile:
    for f in filelist:
        with open(f) as infile:
            outfile.write(infile.read())
        os.remove(f)

subprocess.call(['osascript', '-e', 'display notification "Demo testing done!" with title "Eternity demo test"'])
