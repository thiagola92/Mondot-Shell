import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pymongo"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("run.py", target_name="run", base=base)]

setup(
    name="mondot",
    version="0.0.0",
    description="Mondot shell",
    options={"build_exe": build_exe_options},
    executables=executables,
)
