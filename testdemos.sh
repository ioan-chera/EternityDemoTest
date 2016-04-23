#!/bin/bash

rm demolog.txt
calldoom="eternity-port/eternity -base eternity-port/base -user eternity-port/user -iwad doom -nodraw -nosound -demolog demolog.txt"
calldoom2="eternity-port/eternity -base eternity-port/base -user eternity-port/user -iwad doom -nodraw -nosound -demolog demolog.txt"

shopt -s nocaseglob
for f in $(ls 00_e2m8/*.lmp); do $calldoom -file 00_e2m8/00_e2m8.wad -fastdemo $f; done
shopt -u nocaseglob