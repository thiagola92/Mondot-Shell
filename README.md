# Mondot Shell
Mondot Shell creates an interactive environment between [Mondot](https://github.com/thiagola92/Mondot) and [Python](https://www.python.org/). It execute Python code and return to Mondot the last expression result.

![communication](https://user-images.githubusercontent.com/9352894/135046656-69973ac1-bf75-47ce-ac46-7d7e62168c18.png)

# Requirements
This project use [PDM](https://github.com/pdm-project/pdm) as package and dependency manager.  

Install dependendecies: `pdm install`  
Build executable: `pdm run pyinstaller run.py --onefile --name shell`  

# Run
Python: `python run.py --code-path ./tests/code/none/hello_world.py --tmp-path tmp/tmp.py`  
Executable: `./shell --code-path ./tests/code/none/hello_world.py --tmp-path tmp/tmp.py`  