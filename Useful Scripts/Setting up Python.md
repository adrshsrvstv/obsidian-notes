---
title: Setting up Python The Right Way
subtitle: Or at least how I do it.
author:
  - Adarsh Srivastava
date: 13 December, 2024
tags:
---

## Installing stuff

### macOS

First, DO NOT do these things:

- Touch the default python or pip installation at `/usr/bin/python3` and `/usr/bin/pip3`. They are from Apple and installed with xcode. Ignore them, let them live their life. See [Python Development Environment on MacOS Ventura and Monterey](https://hackercodex.com/guide/python-development-environment-on-mac-osx/)
- Install Anaconda or miniconda or any conda based package. Conda is slow. Mamba is fast but still not entirely PEP compliant. Anaconda installs a whole bunch of stuff on a global environment. Just stick to vanilla python/pip/venv.
- Install python from brew. Brew makes installation convenient but can put things all over the place. Stick with the standard python.org installation. See [Homebrew Python Is Not For You](https://justinmayer.com/posts/homebrew-python-is-not-for-you/)

Now, assuming we are starting from a clean slate (no brew or miniconda installations or paths in bashrc), just download and install the `.dmg` from the python.org site. Ignore the GUI and unrelated scripts. Post that, you should have:

```bash
$ which -a python3 pip3
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
/Library/Frameworks/Python.framework/Versions/3.13/bin/pip3
```

## Virtual Environments

Always use venvs. Keep them in your home folder in `.venvs`

- Create a venv with

```bash
$ python3 -m venv <venv_path>
```

- Activate with

```bash
$ source <venv_path>/bin/activate
```

And then run:
```bash
$ python3 -m pip install --upgrade pip setuptools wheel
```

Once done, deactivate with simply `deactivate`.

> [!Tip] Creating Venv with different python version
> 
> Venvs only reference the original python binary. So to create a venv with another python version, you need to call the venv creation module from that python version. So first install the version you need from python.org and then create venv by calling that particular python version, like:
> 
> `python3.8.1 -m venv <path_to_venv>`
> 
> Make sure you install python with only these options:
> 
> ![](attachments/Screenshot%202024-12-19%20at%207.23.43%20PM.png)
> 
> Then do Install Certificates from the application folder for proper SSL certificates to be installed.

Create a default venv where you only install the basic packages such as numpy, pandas, matplotlib, etc. No specialized packaged at all - anything that can cause conflicts goes in its own venv. 

INSTALL NOTHING WITHOUT A VENV. ONLY PYTHON AND PIP SHOULD BE THERE GLOBALLY.

## Installing Packages

Use pip, always. Use within the virtual environment, always. To get the requirements.txt file:

```bash
$ python3 -m pip freeze > requirements.txt
```

To install from requirements:
```bash
$ python3 -m pip install -r requirements.txt
```

## Installing Jupyter

```bash
pip install jupyterlab
```
