import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
	base = "win32GUI"

setup(name="TicTac",
	version = "1.0",
	description="Fun computer game",
	options={'build_exe': {'include_files': include_files}},
	executables=[Executable("GameForShreya.py", base=base)])