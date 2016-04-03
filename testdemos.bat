@echo off

del demolog.txt
set calldoom=c:\users\ioan_chera\development\eternity\vc2012\release\eternity -base c:\users\ioan_chera\development\eternity\base -user c:\users\ioan_chera\development\eternity\user -iwad doom -nodraw -nosound -demolog demolog.txt
set calldoom2=c:\users\ioan_chera\development\eternity\vc2012\release\eternity -base c:\users\ioan_chera\development\eternity\base -user c:\users\ioan_chera\development\eternity\user -iwad doom2 -nodraw -nosound -demolog demolog.txt

for /f %%f in ('dir /b 00_e2m8\*.lmp') do %calldoom% -file 00_e2m8\00_e2m8.wad -fastdemo 00_e2m8\%%f
%calldoom% -deh betaskulltest\betaskull.bex -fastdemo betaskulltest\betaskul
for /f %%f in ('dir /b competn\doom\*.lmp') do %calldoom% -fastdemo competn\doom\%%f
for /f %%f in ('dir /b 01fava\*.lmp') do %calldoom% -file 01fava\fava.wad -fastdemo 01fava\%%f
%calldoom% -file 01fava\crap115\crap115.wad -fastdemo 01fava\crap115\crap115.lmp
for /f %%f in ('dir /b scythe2\*.lmp') do %calldoom2% -file scythe2\scythe2.wad -fastdemo scythe2\%%f
for /f %%f in ('dir /b scythe2\spechits\*.lmp') do %calldoom2% -file scythe2\scythe2.wad -fastdemo scythe2\spechits\%%f -spechit 0x01C09C98
for /f %%f in ('dir /b sodfinal\*.lmp') do %calldoom2% -file sodfinal\sodfinal.wad -fastdemo sodfinal\%%f
for /f %%f in ('dir /b sodfinal\old\*.lmp') do %calldoom2% -file sodfinal\sodfinal.wad sodfinal\sod_old.wad -fastdemo sodfinal\old\%%f
for /f %%f in ('dir /b valiant\*.lmp') do %calldoom2% -file valiant\valiant.wad -fastdemo valiant\%%f
for /f %%f in ('dir /b dr2008v2\*.lmp') do %calldoom2% -file dr2008v2\dr2008v2.wad -bex dr2008v2\dr2008v2.bex -fastdemo dr2008v2\%%f
for /f %%f in ('dir /b 1994tu\*.lmp') do %calldoom2% -file 1994tu\1994tu.wad -fastdemo 1994tu\%%f
for /f %%f in ('dir /b vanguard\*.lmp') do %calldoom2% -file vanguard\vanguard.wad -fastdemo vanguard\%%f
for /f %%f in ('dir /b 1killtng\*.lmp') do %calldoom2% -file 1killtng\1killtng.wad -fastdemo 1killtng\%%f
for /f %%f in ('dir /b 10sector\*.lmp') do %calldoom2% -file 10sector\10sector.wad -fastdemo 10sector\%%f
