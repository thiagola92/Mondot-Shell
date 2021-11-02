# Mondot Shell
Mondot Shell creates an interactive environment between [Mondot](https://github.com/thiagola92/Mondot) and [Python](https://www.python.org/). It execute Python code and return to Mondot the last expression result.

![communication](https://user-images.githubusercontent.com/9352894/135046656-69973ac1-bf75-47ce-ac46-7d7e62168c18.png)

# Requirements

## Build
To build the executable you will need patchelf

**Ubuntu**
```
sudo apt-get install patchelf
```

**Fedora**
```
dnf install patchelf
```

More details at: https://cx-freeze.readthedocs.io/en/latest/installation.html

## Python
Install pip requirements:
```
pip install -r requirements.txt
```

# Build
Create an executable file used by Mondot to run Python code:
```
python setup.py build
```

# Run

## Python script
```
python run.py --input tests/code/hello_world.py --tmp tmp/tmp.py
```

## Executable
```
run --input tests/code/hello_world.py --tmp tmp/tmp.py
```