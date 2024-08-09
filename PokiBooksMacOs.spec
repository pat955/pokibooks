# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.config import Config

a = Analysis(
    [('src/poki_books.py')],
    pathex=[],
    binaries=[],
    datas=[
        ('static/*', 'static'),  # Ensure static files go into a 'static' folder
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
    name='PokiBooks',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,  # Add your macOS code-signing identity here if needed
    entitlements_file=None,  # Add path to your entitlements file if needed
    icon=['static/icon.icns'],  # Use .icns for macOS icons
)

app = BUNDLE(
    exe,
    name='PokiBooks.app',
    icon=['static/icon.icns'],
    bundle_identifier='com.example.pokibooks',  # Replace with your bundle identifier
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
        ],
    },
)

# Collect everything into the final application bundle
coll = COLLECT(
    app,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PokiBooksMacOs'
)
