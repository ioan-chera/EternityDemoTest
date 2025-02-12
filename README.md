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

## IWAD encryption info

This uses commercial and registered game IWADs for some of the demos. To obtain them legally, they exist in an encrypted form in a URL downloaded from the scripts here. I no longer have the necessary encryption keys, and the decryption key is stored in a secret variable on CI.

In case of loss of encrypted IWADs, assuming you have all the necessary IWADs, such as Doom, Doom II, The Plutonia Experiment and Heretic, the procedure involves having the `openssl` utility, and doing the following:

1. Generating private key
```
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
```

2. Extracting public key
```
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

3. Generating a random 256-bit key for AES encryption
```
openssl rand -out aes.key 32
```

4. Encrypting each IWAD with AES using PBKDF2 and a high iteration count
```
openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -in doom.wad -out doom.wad.enc -kfile aes.key
# same with the other IWADs
```

5. Encrypting the AES key with RSA public key
```
openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in aes.key -out aes.key.enc
```

6. Uploading it all: make sure to upload ONLY the files ending in `*.enc` (delete the rest to be safe!) and then put the private key in a *secret* container on your CI environment, such as GitHub Actions, where only you have access.
