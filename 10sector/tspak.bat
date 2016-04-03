@echo off
:top
cls
echo.
echo        The 10sector
echo        lmp  Collection
echo (requires BOOM, www.teamtnt.com)
echo     =======================
echo We have 3 sets of demo's for you to watch
echo 1) All MAX demo's
echo 2) All MAP 30 contest demo's 
echo 3) All special demo's
echo Make your choice or hit 0 to quit, but remember:
echo    WE KNOW WHERE YOU LIVE!

choice /c:1230/n

if errorlevel 4 goto END
if errorlevel 3 goto SPECIAL
if errorlevel 2 goto CONTEST
if errorlevel 1 goto MAX

:MAX
echo you have chosen to watch the max demo's:
echo we have 32 max demo's for you,
echo please make your choice.
echo ++++++++++++++++++++++++++++++++++++++++
echo.
echo 1) Map01	H) Map 18
echo 2) Map02	I) Map 19
echo 3) Map03	J) Map 20
echo 4) Map04	K) Map 21
echo 5) Map05	L) Map 22
echo 6) Map06	M) Map 23
echo 7) Map07	N) Map 24
echo 8) Map08	O) Map 25
echo 9) Map09	P) Map 26
echo A) Map10	Q) Map 27
echo B) Map11	R) Map 28
echo C) Map12	S) Map 29	recorded by Gemini
echo D) Map13	T) Map 29	recorded by Mike Toliver
echo E) Map14	U) Map 30
echo F) Map15	V) Map 31
echo G) Map17	W) Map 32
echo.
echo X to return to previous menu
echo 0 to quit, but remember:
echo	WE KNOW WHERE YOU LIVE!

choice /c:123456789ABCDEFGHIJKLMNOPQRSTUVWX0/n

if errorlevel 34 goto END
if errorlevel 33 goto TOP
if errorlevel 32 goto MAP32
if errorlevel 31 goto MAP31
if errorlevel 30 goto MAP30
if errorlevel 29 goto MAP29M
if errorlevel 28 goto MAP29G
if errorlevel 27 goto MAP28
if errorlevel 26 goto MAP27
if errorlevel 25 goto MAP26
if errorlevel 24 goto MAP25
if errorlevel 23 goto MAP24
if errorlevel 22 goto MAP23
if errorlevel 21 goto MAP22
if errorlevel 20 goto MAP21
if errorlevel 19 goto MAP20
if errorlevel 18 goto MAP19
if errorlevel 17 goto MAP18
if errorlevel 16 goto MAP17
if errorlevel 15 goto MAP15
if errorlevel 14 goto MAP14
if errorlevel 13 goto MAP13
if errorlevel 12 goto MAP12
if errorlevel 11 goto MAP11
if errorlevel 10 goto MAP10
if errorlevel 9 goto MAP09
if errorlevel 8 goto MAP08
if errorlevel 7 goto MAP07
if errorlevel 6 goto MAP06
if errorlevel 5 goto MAP05
if errorlevel 4 goto MAP04
if errorlevel 3 goto MAP03
if errorlevel 2 goto MAP02
if errorlevel 1 goto MAP01



:MAP01
boom -file 10sector -playdemo ts01-025
goto MAX

:MAP02
boom -file 10sector -playdemo ts02-238
goto MAX

:MAP03
echo no demo yet
goto MAX

:MAP04
boom -file 10sector -playdemo ts04-221
goto MAX

:MAP05
boom -file 10sector -playdemo ts05-215
goto MAX

:MAP06
boom -file 10sector -playdemo ts06-352
goto MAX

:MAP07
echo no demo yet
goto MAX

:MAP08
boom -file 10sector -playdemo ts08-940
goto MAX

:MAP09
boom -file 10sector -playdemo ts09-556
goto MAX

:MAP10
boom -file 10sector -playdemo ts10-341
goto MAX

:MAP11
boom -file 10sector -playdemo ts11-611
goto MAX

:MAP12
boom -file 10sector -playdemo ts12-514
goto MAX

:MAP13
boom -file 10sector -playdemo ts13-450
goto MAX

:MAP14
boom -file 10sector -playdemo ts14-319
goto MAX

:MAP15
echo no demo yet
goto MAX

:MAP17
boom -file 10sector -playdemo ts171304
goto MAX

:MAP18
boom -file 10sector -playdemo ts18-512
goto MAX

:MAP19
boom -file 10sector -playdemo ts19-316
goto MAX

:MAP20
boom -file 10sector -playdemo ts20-1019
goto MAX

:MAP21
boom -file 10sector -playdemo ts21-1933
goto MAX

:MAP22
no demo yet
goto MAX

:MAP23
boom -file 10sector -playdemo ts23-548
goto MAX

:MAP24
boom -file 10sector -playdemo ts24-907
goto MAX

:MAP25
boom -file 10sector -playdemo ts25-332
goto MAX

:MAP26
boom -file 10sector -playdemo ts26-1528
goto MAX

:MAP27
boom -file 10sector -playdemo ts27-721
goto MAX

:MAP28
boom -file 10sector -playdemo ts28-1039
goto MAX

:MAP29G
boom -file 10sector -playdemo ts29-2251
goto MAX

:MAP29M
boom -file 10sector -playdemo ts295321
goto MAX

:MAP30
boom -file 10sector -playdemo ts30-414
goto MAX

:MAP31
echo no demo yet
goto MAX

:MAP32
boom -file 10sector -playdemo ts321213
goto MAX

:CONTEST
echo you have chosen to watch the contest demo's of MAP30:
echo we have 04 contest demo's for you,
echo please make your choice.
echo ++++++++++++++++++++++++++++++++++++++++
echo.
echo 1) MAP30 recorded by Gemini in	4:14
echo 2) MAP30 recorded by Vrooomer in	4:38
echo 3) MAP30 recorded by Opulent in	5:54
echo 4) MAP30 recorded by Vorpal in	6:05
echo.
echo X to return to previous menu
echo 0 to quit, but remember:
echo	WE KNOW WHERE YOU LIVE!

Choice /c:1234x0/n

if errorlevel 6 goto END
if errorlevel 5 goto TOP
if errorlevel 4 goto MAP30VO
if errorlevel 3 goto MAP30OP
if errorlevel 2 goto MAP30VR
if errorlevel 1 goto MAP30GE

:MAP30GE
boom -file 10sector -playdemo ts30-414
goto CONTEST

:MAP30VR
boom -file 10sector -playdemo ts30-438
goto CONTEST

:MAP30OP
boom -file 10sector -playdemo ts30-554
goto CONTEST

:MAP30VO
boom -file 10sector -playdemo ts30-605
goto CONTEST

SPECIAL:
echo you have chosen to watch the special demo's:
echo we have 07 special demo's for you,
echo please make your choice.
echo ++++++++++++++++++++++++++++++++++++++++
echo.
echo Special demo's by Vrooomer:
echo.
echo 1) speed demo of MAP14 on UV in		0:53
echo 2) YTITD speed demo of MAP14 SKILL 1 in	0:33
echo 3) speed demo of MAP30 on UV in		0:48
echo.
echo Special demo's by Opulent:
echo.
echo 4) Nightmare demo of MAP09 in		2:44
echo.
echo Special demo's by .AC.:
echo.
echo 5) Speed demo of MAP12 on UV in		0:32
echo 6) Pacifist demo of MAP12 on UV in		0:42
echo.
echo Special demo's by the mole:
echo.
echo 7) Speed demo of MAP24 on UV in		0:13
echo.
echo X to return to previous menu
echo 0 to quit, but remember:
echo	WE KNOW WHERE YOU LIVE!

choice c:/12345670x/n

if errorlevel 9 goto END
if errorlevel 8 goto TOP
if errorlevel 7 goto MAP24S
if errorlevel 6 goto MAP12P
if errorlevel 5 goto MAP12S
if errorlevel 4 goto MAP09N
if errorlevel 3 goto MAP30S
if errorlevel 2 goto MAP14S1
if errorlevel 1 goto MAP14S

:MAP14S
boom -file 10sector -playdemo ts14s053
goto SPECIAL

:MAP14S1
boom -file 10sector -playdemo ts14sk1
goto SPECIAL

:MAP30S
boom -file 10sector -playdemo ts30s048
goto SPECIAL

:MAP09N
boom -file 10sector -playdemo ts09n244
goto SPECIAL

:MAP12S
boom -file 10sector -playdemo ts12s032
goto SPECIAL

:MAP12P
boom -file 10sector -playdemo ts12p042
goto SPECIAL

:MAP24S
boom -file 10sector -playdemo ts24s013
goto SPECIAL

:end
@echo cYa!
@pause
cls
@echo Thanks for watching!
