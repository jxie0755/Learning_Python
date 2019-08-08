# -*- mode: python -*-

block_cipher = None


a = Analysis(['connect_n_game_classic.py'],
             pathex=['C:\\Users\\jxie0\\Documents\\GitHub\\Learning_Python\\ZZProject\\ConnectN\\Classic'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='connect_n_game_classic',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
