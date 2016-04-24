#!/usr/bin/env python
import multiprocessing
import os
import subprocess
from joblib import Parallel, delayed

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
    files = os.listdir(item[1])
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

Parallel(n_jobs=cpu_count)(delayed(subprocess.call)(a) for a in commands_list)

filelist = [ os.path.join('temp-logs', f) for f in os.listdir("temp-logs") if f.endswith(".txt") ]

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
