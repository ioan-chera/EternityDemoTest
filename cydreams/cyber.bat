echo OFF
cls
echo. ****************************
echo. * CYBERDREAMS installation *
echo. ****************************
echo.
echo.  CYBERDREAMS includes a special Dehacked patch
echo.  which MUST be installed so that the game
echo.  runs correctly. If you just load the PWAD
echo.  file it won't.
echo.
echo.  This "CYBER.BAT" will write a new DOOMHACK.EXE
echo.  file and then it will rename it to CYDREAMS.EXE. If
echo.  you have a previous DOOMHACK.EXE this install program
echo.  will make a temporary rename of it as DOOMHACK.OLD
echo.  till you exit Cyberdreams.
echo.
echo.  Just answer "yes" to the following question.
echo.
echo.
pause
cls
if exist doomhack.old del doomhack.old
if exist dehacked.ini ren dehacked.ini dehacked.in2
if exist doomhack.exe ren doomhack.exe doomhack.old
dehacked -load cyber110.deh
ren doomhack.exe cydreams.exe
echo.
echo. That's it! Cyberdreams is ready to run.
echo.
pause
cydreams -game cyber110.wad
if exist doomhack.old ren doomhack.old doomhack.exe
if exist dehacked.in2 ren dehacked.in2 dehacked.ini
del cydreams.exe



