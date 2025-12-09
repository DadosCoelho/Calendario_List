@echo off
chcp 65001 >nul

:MENU
cls
echo ========================================
echo    CALENDARIO LIST - MENU PRINCIPAL
echo ========================================
echo.
echo  1. 🚀 Executar em Modo Desenvolvimento
echo  2. 📦 Compilar Executável - Navegador
echo  3. 🪟 Compilar Executável - Janela Dedicada
echo  4. 🧹 Limpar Arquivos de Build
echo  5. 🔥 Limpeza Forçada (se opção 4 falhar)
echo  6. 📋 Instalar/Atualizar Dependências
echo  7. ℹ️  Informações do Sistema
echo  0. ❌ Sair
echo.
echo ========================================
set /p OPCAO="Escolha uma opção: "

if "%OPCAO%"=="1" goto DEV
if "%OPCAO%"=="2" goto BUILD
if "%OPCAO%"=="3" goto BUILD_WEBVIEW
if "%OPCAO%"=="4" goto CLEAN
if "%OPCAO%"=="5" goto FORCE_CLEAN
if "%OPCAO%"=="6" goto DEPS
if "%OPCAO%"=="7" goto INFO
if "%OPCAO%"=="0" goto SAIR

echo.
echo [ERRO] Opção inválida!
timeout /t 2 >nul
goto MENU

:DEV
cls
echo ========================================
echo     EXECUTAR EM MODO DESENVOLVIMENTO
echo ========================================
echo.
call run_dev.bat
goto MENU

:BUILD
cls
echo ========================================
echo    COMPILAR EXECUTÁVEL - NAVEGADOR
echo ========================================
echo.
call build.bat
goto MENU

:BUILD_WEBVIEW
cls
echo ========================================
echo   COMPILAR EXECUTÁVEL - JANELA DEDICADA
echo ========================================
echo.
call build_webview.bat
goto MENU

:CLEAN
cls
call clean.bat
goto MENU

:FORCE_CLEAN
cls
call force_clean.bat
goto MENU

:DEPS
cls
echo ========================================
echo    INSTALAR/ATUALIZAR DEPENDÊNCIAS
echo ========================================
echo.

if exist "venv\" (
    echo [INFO] Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo [INFO] Criando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo.
echo [INFO] Atualizando pip...
python -m pip install --upgrade pip

echo.
echo [INFO] Instalando/Atualizando dependências...
pip install -r requirements.txt

echo.
echo [OK] Dependências instaladas com sucesso!
echo.
pause
goto MENU

:INFO
cls
echo ========================================
echo       INFORMAÇÕES DO SISTEMA
echo ========================================
echo.

python --version 2>nul
if errorlevel 1 (
    echo [ERRO] Python não encontrado!
) else (
    echo [OK] Python instalado
)
echo.

if exist "venv\" (
    echo [OK] Ambiente virtual: Existe
    call venv\Scripts\activate.bat
    echo.
    echo Pacotes instalados:
    echo.
    pip list
) else (
    echo [AVISO] Ambiente virtual: Não existe
)
echo.

if exist "dist\CalendarioList.exe" (
    echo [OK] Executável compilado: Sim
    for %%A in ("dist\CalendarioList.exe") do (
        echo     Tamanho: %%~zA bytes
        echo     Data: %%~tA
    )
) else (
    echo [AVISO] Executável compilado: Não
)
echo.

echo Arquivos do projeto:
echo.
dir /b *.py 2>nul
echo.

echo ========================================
pause
goto MENU

:SAIR
cls
echo.
echo Até logo! 👋
echo.
timeout /t 2 >nul
exit