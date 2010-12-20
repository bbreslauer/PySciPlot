# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), 'pysciplot.py'],
             pathex=['/home/ben/programming/pysciplot/branches/mpl'],
             hookspath=['/home/ben/programming/pysciplot/branches/mpl/pyinstaller'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
#a.scripts,
          a.scripts + [('v', '', 'OPTION')],
          exclude_binaries=1,
          name=os.path.join('build/pyi.linux2/psp', 'psp'),
          debug=True,
          strip=False,
          upx=True,
          console=1 )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'psp'))
