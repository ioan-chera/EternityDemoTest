@echo off

if "%2"=="" goto START
if "%3"=="" goto HARD
if "%3"=="0" goto NOMON

Doom2 -Devparm -File RESOURCE.WAD #%1.WAD -Warp %2 -Skill %3 %4 %5 %6 %7
goto END

:START
Doom2 -File RESOURCE.WAD #%1.WAD
goto END

:HARD
Doom2 -Devparm -File RESOURCE.WAD #%1.WAD -Warp %2 -Skill 4
goto END

:NOMON
Doom2 -Devparm -File RESOURCE.WAD #%1.WAD -Warp %2 -NoMonsters %4 %5 %6 %7
:END
