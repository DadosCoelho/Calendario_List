@echo off
chcp 65001 >nul
cls

echo ========================================
echo     LIMPEZA FORÇADA - CALENDARIO LIST
echo ========================================
echo.

echo [INFO] Este script irá:
echo   1. Fechar CalendarioList.exe se estiver rodando
echo   2. Aguardar liberação de arquivos
echo   3. Forçar remoção de build/ e dist/
echo.

REM Mata o processo se estiver rodando
echo [INFO] Verificando processos...
tasklist /FI "IMAGENAME eq CalendarioList.exe" 2>NUL | find /I /N "CalendarioList.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [AVISO] CalendarioList.exe detectado em execução!
    echo [INFO] Forçando encerramento...
    taskkill /F /IM CalendarioList.exe >nul 2>&1
    echo [OK] Processo encerrado!
    timeout /t 3 >nul
) else (
    echo [OK] Nenhum processo em execução.
)
echo.

REM Remove build
if exist "build\" (
    echo [INFO] Removendo pasta build/...
    rmdir /s /q build 2>nul
    timeout /t 1 >nul
    
    if exist "build\" (
        echo [AVISO] Tentando forçar remoção...
        rd /s /q build 2>nul
        timeout /t 1 >nul
    )
    
    if exist "build\" (
        echo [ERRO] Não foi possível remover build/
        echo Feche todos os programas que possam estar usando os arquivos.
    ) else (
        echo [OK] Pasta build/ removida!
    )
)

REM Remove executável específico
if exist "dist\CalendarioList.exe" (
    echo [INFO] Removendo CalendarioList.exe...
    del /f /q "dist\CalendarioList.exe" 2>nul
    timeout /t 1 >nul
    
    if exist "dist\CalendarioList.exe" (
        echo [AVISO] Tentando forçar remoção...
        attrib -r -s -h "dist\CalendarioList.exe" >nul 2>&1
        del /f /q "dist\CalendarioList.exe" 2>nul
    )
    
    if exist "dist\CalendarioList.exe" (
        echo [ERRO] Executável ainda está bloqueado!
    ) else (
        echo [OK] Executável removido!
    )
)

REM Remove dist
if exist "dist\" (
    echo [INFO] Removendo pasta dist/...
    rmdir /s /q dist 2>nul
    timeout /t 1 >nul
    
    if exist "dist\" (
        echo [AVISO] Tentando forçar remoção...
        rd /s /q dist 2>nul
        timeout /t 1 >nul
    )
    
    if exist "dist\" (
        echo [ERRO] Não foi possível remover dist/
    ) else (
        echo [OK] Pasta dist/ removida!
    )
)

REM Remove spec gerado automaticamente
if exist "CalendarioList.spec" (
    echo [INFO] Removendo CalendarioList.spec...
    del /q CalendarioList.spec 2>nul
    echo [OK] Spec removido!
)

REM Remove __pycache__
echo [INFO] Removendo cache Python...
for /d /r %%i in (__pycache__) do (
    if exist "%%i" (
        rmdir /s /q "%%i" 2>nul
    )
)
echo [OK] Cache limpo!

echo.
echo ========================================
echo          LIMPEZA CONCLUÍDA!
echo ========================================
echo.

REM Verifica se ainda há arquivos
if exist "build\" (
    echo [AVISO] build/ ainda existe
)
if exist "dist\" (
    echo [AVISO] dist/ ainda existe
)
if not exist "build\" (
    if not exist "dist\" (
        echo [OK] Todos os arquivos foram removidos!
    )
)

echo.
pause