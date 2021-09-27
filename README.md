# Mondot Shell
Mondot Shell creates an interactive environment between [Mondot](https://github.com/thiagola92/Mondot) and [Python](https://www.python.org/). It execute Python code and return to Mondot the last expression result.

# Run
Run as any other Python script:
```
python run.py --input tests/code/hello_world.py --tmp tmp/tmp.py
```

If you have build an executable, use it like:
```
run --input tests/code/hello_world.py --tmp tmp/tmp.py
```


# Build
Create an executable file used by Mondot to run Python code:
```
python setup.py build
```

