@echo off
chcp 65001 >nul
cls

echo ========================================
echo     CALENDARIO LIST - CLEAN SYSTEM
echo ========================================
echo.

echo [AVISO] Este script irá deletar:
echo   - Pasta build/
echo   - Pasta dist/
echo   - Arquivo CalendarioList.spec
echo   - Arquivos __pycache__
echo.
echo Deseja continuar? (S/N)
set /p CONFIRMAR=

if /i not "%CONFIRMAR%"=="S" (
    echo.
    echo [INFO] Operação cancelada.
    pause
    exit /b 0
)

echo.
echo [INFO] Limpando arquivos de build...

echo [INFO] Verificando processos em execução...
tasklist /FI "IMAGENAME eq CalendarioList.exe" 2>NUL | find /I /N "CalendarioList.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [AVISO] CalendarioList.exe está em execução!
    echo [INFO] Encerrando processo...
    taskkill /F /IM CalendarioList.exe >nul 2>&1
    timeout /t 2 >nul
)

if exist "build\" (
    echo [INFO] Removendo pasta build/...
    rmdir /s /q build 2>nul
    timeout /t 1 >nul
    if exist "build\" (
        echo [AVISO] Não foi possível remover build/ completamente
    ) else (
        echo [OK] Pasta build/ removida!
    )
)

if exist "dist\CalendarioList.exe" (
    echo [INFO] Removendo executável...
    del /f /q "dist\CalendarioList.exe" 2>nul
    timeout /t 1 >nul
)

if exist "dist\" (
    echo [INFO] Removendo pasta dist/...
    rmdir /s /q dist 2>nul
    timeout /t 1 >nul
    if exist "dist\" (
        echo [AVISO] Não foi possível remover dist/ completamente
    ) else (
        echo [OK] Pasta dist/ removida!
    )
)

if exist "CalendarioList.spec" (
    echo [INFO] Removendo CalendarioList.spec...
    del /q CalendarioList.spec
    echo [OK] CalendarioList.spec removido!
)

echo [INFO] Removendo __pycache__...
for /d /r %%i in (__pycache__) do (
    if exist "%%i" (
        rmdir /s /q "%%i"
    )
)
echo [OK] __pycache__ removido!

echo.
echo ========================================
echo       LIMPEZA CONCLUÍDA COM SUCESSO!
echo ========================================
echo.
pause