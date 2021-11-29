# EternityDemoTest
Eternity demo regression testing set

This is a set of demos to test Eternity with. The list will grow as I need more demos to test.

Important: you need the Eternity Engine port.

You can get development releases (for Windows and macOS) from https://devbuilds.drdteam.org/eternity/ and https://devbuilds.drdteam.org/eternity-mac/. You can build it from source from github.com/team-eternity/Eternity.

## How to use

Create a folder in your local copy, named "eternity-port". Inside it, place a link (or a copy) of the compiled Eternity executable and the user/ and base/ folders.

Copy or link the DOOM, DOOM2, PLUTONIA and HERETIC IWADs to the source root. You'll need them for the demos.

You need Python. You need to have the `joblib` package installed. You can install it with `pip` using `pip install joblib`. Under Linux and Windows you also need to install `py-notifier`. Windows in addition requires `win10toast`. At the moment of this writing, EternityDemoTest has been tested on macOS and Windows.

Run **testdemos.py**. It will launch Eternity without UI on as many parallel instances as there are processor cores.

Optional argument: `--cpu <number_of_cores>`. If used, it can limit the work to a few of the processors. See `--help` for more command-line options.

## Caution
1. When git-cloning: size may be significant, and it is going to grow.
2. It may take awhile to run and during this time it may slow down your workflow. You can always cancel it with Ctrl+C however. You can try using the `--cpu` parameter to reduce the intensity.
