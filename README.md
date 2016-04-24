# EternityDemoTest
Eternity demo regression testing set

This is a set of demos to test Eternity with. The list will grow as I need more demos to test.

Important: you need Eternity from github.com/team-eternity/Eternity, compiled from the demo-test branch (not master!).

How to use: create a folder in your local copy, named "eternity-port". Inside it, place a link (or a copy) of the demo-test compiled Eternity executable and the user/ and base/ folders. 

You will need Python 2.7. Run **testdemos.py**. It will launch Eternity without UI on as many parallel instances as there are processor cores.

## Caution
1. When git-cloning: size may be signifiant, and it is going to grow.
2. It may not work on your platform. So far it has been tested on OS X.
3. It may take awhile to run.
