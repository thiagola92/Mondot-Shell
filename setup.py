import sys

from cx_Freeze import Executable, setup

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(executables=[Executable("run.py", base=base)])
