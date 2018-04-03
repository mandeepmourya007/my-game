import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
executables=[cx_Freeze.Executable("mainsnake.py")]
cx_Freeze.setup(
    name="SNAKE GAME",
    options={"build_exe":{"packages":["pygame"],"include_files":[],
                          }},
    description="snake game created by mandeep",
    executables=executables
    )
	



os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'
