# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), '../src/main.py'],
             pathex=['/home/ben/programming/pysciplot-git/packager'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'pspone'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
