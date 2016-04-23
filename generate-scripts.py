#!/usr/bin/env python

# 0. Get data from .data
with open('demo-list.data', 'r') as demolist:
    s = demolist.readlines()
items = []
for l in s:
    item = l.split()
    if len(item) < 2:
        continue
    items.append(item)
    

# 1. Generate bat for Windows
with open('testdemos.bat.in', 'r') as myfile:
    data = myfile.read().replace('\n', '\r\n')  # be like Windows

for item in items:
    if item[0] not in {'1', '2'}:
        continue
    item1 = item[1].replace('/', '\\')
    if item[0] == '1':
        data += "\r\nfor /f %%f in ('dir /b " + item1 + "\\*.lmp') do %calldoom% -fastdemo " + item1 + "\\%%f"
    elif item[0] == '2':
        data += "\r\nfor /f %%f in ('dir /b " + item1 + "\\*.lmp') do %calldoom2% -fastdemo " + item1 + "\\%%f"
    if len(item) > 2:
        for subitem in item[2:]:
            data += " " + subitem
data += '\r\n'

with open("testdemos.bat", "w") as text_file:
    text_file.write(data)
    
# 2. Generate sh for Mac (TODO: case-sensitive systems)
with open('testdemos.sh.in', 'r') as myfile:
    data = myfile.read()

for item in items:
    if item[0] not in {'1', '2'}:
        continue
    
    if item[0] == '1':
        data += '\nfind ' + item[1] + ' -iname "*.lmp" | while read f; do $calldoom -fastdemo "$f"'
    elif item[0] == '2':
        data += '\nfind ' + item[1] + ' -iname "*.lmp" | while read f; do $calldoom2 -fastdemo "$f"'
    if len(item) > 2:
        for subitem in item[2:]:
            data += " " + subitem
    data += "; done"

with open("testdemos.sh", "w") as text_file:
    text_file.write(data)
