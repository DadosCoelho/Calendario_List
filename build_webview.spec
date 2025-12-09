# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app_webview.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('config_tabelas.py', '.'),
        ('simulador.py', '.'),
        ('relatorio_top_mensal.py', '.'),
        ('relatorio_dependencias.py', '.'),
        ('relatorio_tamanho_listas.py', '.'),
        ('relatorio_listas_por_intervalo.py', '.'),
        ('relatorio_sorteios_pick.py', '.'),
    ],
    hiddenimports=[
        'flask',
        'webview',
        'config_tabelas',
        'simulador',
        'relatorio_top_mensal',
        'relatorio_dependencias',
        'relatorio_tamanho_listas',
        'relatorio_listas_por_intervalo',
        'relatorio_sorteios_pick',
        'clr',
        'webview.platforms.winforms',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CalendarioList',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)