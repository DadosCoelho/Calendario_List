@echo off
chcp 65001 >nul
cls

echo ========================================
echo  CALENDARIO LIST - BUILD JANELA DEDICADA
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não encontrado!
    echo Por favor, instale Python 3.8 ou superior.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.

REM Verifica se venv existe
if exist "venv\" (
    echo [INFO] Ambiente virtual encontrado.
) else (
    echo [INFO] Criando ambiente virtual...
    python -m venv venv
    if errorlevel 1 (
        echo [ERRO] Falha ao criar ambiente virtual!
        pause
        exit /b 1
    )
    echo [OK] Ambiente virtual criado!
)
echo.

REM Ativa o ambiente virtual
echo [INFO] Ativando ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERRO] Falha ao ativar ambiente virtual!
    pause
    exit /b 1
)
echo [OK] Ambiente virtual ativado!
echo.

REM Atualiza pip
echo [INFO] Atualizando pip...
python -m pip install --upgrade pip >nul 2>&1
echo [OK] Pip atualizado!
echo.

REM Instala dependências
echo [INFO] Instalando dependências...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependências!
    pause
    exit /b 1
)
echo [OK] Dependências instaladas!
echo.

REM Instala pythonnet (necessário para pywebview no Windows)
echo [INFO] Instalando pythonnet para pywebview...
pip install pythonnet
echo [OK] pythonnet instalado!
echo.

REM Limpa builds anteriores
echo [INFO] Verificando processos em execução...
tasklist /FI "IMAGENAME eq CalendarioList.exe" 2>NUL | find /I /N "CalendarioList.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [AVISO] CalendarioList.exe está em execução!
    echo [INFO] Encerrando processo...
    taskkill /F /IM CalendarioList.exe >nul 2>&1
    timeout /t 2 >nul
)

if exist "build\" (
    echo [INFO] Limpando build anterior...
    rmdir /s /q build 2>nul
)

if exist "dist\CalendarioList.exe" (
    echo [INFO] Removendo executável anterior...
    del /f /q "dist\CalendarioList.exe" 2>nul
    timeout /t 1 >nul
)

if exist "dist\" (
    echo [INFO] Limpando distribuição anterior...
    rmdir /s /q dist 2>nul
)
echo.

REM Executa PyInstaller
echo [INFO] Compilando aplicação com janela dedicada...
echo.
pyinstaller build_webview.spec
if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao compilar aplicação!
    pause
    exit /b 1
)

echo.
echo ========================================
echo        BUILD CONCLUÍDO COM SUCESSO!
echo ========================================
echo.
echo O executável está em: dist\CalendarioList.exe
echo.
echo OBSERVAÇÃO: Esta versão abre em uma JANELA DEDICADA
echo (não no navegador padrão)
echo.
echo Deseja testar o executável agora? (S/N)
set /p TESTAR=

if /i "%TESTAR%"=="S" (
    echo.
    echo [INFO] Iniciando aplicação...
    start "" "dist\CalendarioList.exe"
)

echo.
echo Pressione qualquer tecla para sair...
pause >nul