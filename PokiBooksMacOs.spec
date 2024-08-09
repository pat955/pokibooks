# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    [('src/poki_books.py'),
    ],
    pathex=[],
    binaries=[],
    datas=[
        ('static/*', 'static')  # Ensure static files go into a 'static' folder| add readme
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)



pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    name='PokiBooks.app',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['static/icon.ico'],
)

app = BUNDLE(exe,
    name='PokiBooks.app',
    icon=['static/icon.icns'],
    bundle_identifier=None,
    version='0.0.1',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'My File Format',
                'CFBundleTypeIconFile': 'MyFileIcon.icns',
                'LSItemContentTypes': ['com.example.myformat'],
                'LSHandlerRank': 'Owner'
                }
            ]
        },
     )


coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PokiBooksMacOs'
)
