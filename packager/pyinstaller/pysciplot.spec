# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), 'pysciplot.py'],
             pathex=['/home/ben/programming/pysciplot/branches/mpl'],
             hookspath=['/home/ben/programming/pysciplot/branches/mpl/pyinstaller'])

pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'pysciplot'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
