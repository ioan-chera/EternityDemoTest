@echo off

del demolog.txt
set calldoom=c:\users\ioan_chera\development\eternity\vc2012\release\eternity -base c:\users\ioan_chera\development\eternity\base -user c:\users\ioan_chera\development\eternity\user -iwad doom -nodraw -nosound -demolog demolog.txt
set calldoom2=c:\users\ioan_chera\development\eternity\vc2012\release\eternity -base c:\users\ioan_chera\development\eternity\base -user c:\users\ioan_chera\development\eternity\user -iwad doom2 -nodraw -nosound -demolog demolog.txt

for /f %%f in ('dir /b %1\*.lmp') do %calldoom2% -file %1\%2.wad -fastdemo %1\%%f
