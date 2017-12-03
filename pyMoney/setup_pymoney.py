import os
import os.path
import sys
import time
import sqlite3
import datetime


from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = r'C:\Users\Ramalho\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ramalho\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


options1 = {
    'build_exe':
	{
        'include_files':
			[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
			os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll'),
			],
			
		'packages':
			[
			
			 'time', 'sys', 'sqlite3', 'datetime'
			],

    "optimize": 2
    },
}





setup(
    options = options1,
    name="pyMoney",
    version="0.1",
    description="py_money",
    executables=[Executable("main.py", base="Win32GUI")],
    shortcutName="pyMoney N.M.O",
    shortcutDir="DesktopFolder",
    
    )
    





