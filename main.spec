# -*- mode: python -*-
a = Analysis(['main.pyx'],
             pathex=['D:\\Dropbox\\python\\GitHub\\REPO\\TabbyLogger'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'main.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name=os.path.join('dist', 'main.exe.app'))
