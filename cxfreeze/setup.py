import sys

sys.path.insert(1, '../src/')

from cx_Freeze import setup, Executable

excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']

exe = Executable(
        script='../src/main.py',
        excludes=excludes,
        )

buildOptions = dict(
        packages = ['modules'],
        excludes = excludes,
        )

setup(
        name = 'psp-pyg',
        version = '0.1',
        description = 'PySciPlot with PyGraphene',
        options = dict(build_exe = buildOptions),
        executables = [exe],
        )

