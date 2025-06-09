# main.spec
#
# PyInstaller spec file for building the application.
#
# Usage:
#   pyinstaller main.spec
#
# This file defines how PyInstaller should bundle your Python application.
# For more information, see: https://pyinstaller.org/en/stable/spec-files.html

# -*- mode: python ; coding: utf-8 -*-

import sys, os
from cx_Freeze import Executable, setup  # (Optional: Only needed if using cx_Freeze features)

block_cipher = None  # Used for encrypting Python bytecode (optional)

# Analysis step:
# - 'src/main.py' is the entry point.
# - pathex: additional paths to search for imports.
# - binaries, datas: additional files to include.
# - hiddenimports: modules PyInstaller can't detect automatically.
# - excludes: modules to exclude.
a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

# PYZ step: Packages Python modules into a .pyz archive.
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

# EXE step: Builds the final executable.
# - name: output executable name.
# - debug: include debug info.
# - upx: use UPX to compress the executable.
# - console: True for console app, False for windowed app.
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)
# onefile ----------------------------------------------------------------
