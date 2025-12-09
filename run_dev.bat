@echo off
chcp 65001 >nul
cls

echo ========================================
echo   CALENDARIO LIST - MODO DESENVOLVIMENTO
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

REM Verifica se venv existe
if exist "venv\" (
    echo [INFO] Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo [INFO] Criando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
    
    echo [INFO] Instalando dependências...
    pip install -r requirements.txt
)
echo.

REM Executa a aplicação
echo [INFO] Iniciando servidor de desenvolvimento...
echo.
echo ========================================
echo   Servidor rodando em: http://127.0.0.1:5000
echo   Pressione Ctrl+C para parar
echo ========================================
echo.

python app.py

pause