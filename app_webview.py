from flask import Flask, render_template, jsonify, send_file
import os
import sys
import webview
from threading import Thread
import json

# Importações do projeto original
from config_tabelas import tabela_numeros
from simulador import gerar_dados_simulados
from relatorio_top_mensal import gerar_relatorio_top_mensal
from relatorio_dependencias import gerar_relatorio_dependencias
from relatorio_tamanho_listas import gerar_relatorio_tamanho_listas
from relatorio_listas_por_intervalo import gerar_relatorio_listas_por_intervalo
from relatorio_sorteios_pick import gerar_relatorio_sorteios_pick

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/gerar-simulacao', methods=['POST'])
def gerar_simulacao():
    try:
        gerar_dados_simulados(tabela_numeros)
        return jsonify({'success': True, 'message': 'Simulação concluída com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})

@app.route('/api/relatorio-top-mensal', methods=['GET'])
def relatorio_top_mensal():
    arquivo = "dados_simulados_br.csv"
    if not os.path.exists(arquivo):
        return jsonify({'success': False, 'message': 'Arquivo de simulação não encontrado!'})
    
    try:
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            gerar_relatorio_top_mensal(arquivo, tabela_numeros)
        
        output = f.getvalue()
        return jsonify({'success': True, 'data': output})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})

@app.route('/api/relatorio-dependencias', methods=['GET'])
def relatorio_dependencias():
    arquivo = "dados_simulados_br.csv"
    if not os.path.exists(arquivo):
        return jsonify({'success': False, 'message': 'Arquivo de simulação não encontrado!'})
    
    try:
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            gerar_relatorio_dependencias(arquivo)
        
        output = f.getvalue()
        return jsonify({'success': True, 'data': output})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})

@app.route('/api/relatorio-tamanho-listas', methods=['GET'])
def relatorio_tamanho_listas():
    arquivo = "dados_simulados_br.csv"
    if not os.path.exists(arquivo):
        return jsonify({'success': False, 'message': 'Arquivo de simulação não encontrado!'})
    
    try:
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            gerar_relatorio_tamanho_listas(arquivo)
        
        output = f.getvalue()
        return jsonify({'success': True, 'data': output})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})

@app.route('/api/relatorio-listas-intervalo', methods=['GET'])
def relatorio_listas_intervalo():
    arquivo = "dados_simulados_br.csv"
    if not os.path.exists(arquivo):
        return jsonify({'success': False, 'message': 'Arquivo de simulação não encontrado!'})
    
    try:
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            gerar_relatorio_listas_por_intervalo(arquivo)
        
        output = f.getvalue()
        return jsonify({'success': True, 'data': output})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})

@app.route('/api/relatorio-sorteios-pick', methods=['GET'])
def relatorio_sorteios_pick():
    arquivo = "dados_simulados_br.csv"
    if not os.path.exists(arquivo):
        return jsonify({'success': False, 'message': 'Arquivo de simulação não encontrado!'})
    
    try:
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            gerar_relatorio_sorteios_pick(arquivo)
        
        output = f.getvalue()
        return jsonify({'success': True, 'data': output})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})

@app.route('/api/download-csv', methods=['GET'])
def download_csv():
    arquivo = "dados_simulados_br.csv"
    
    # Verifica se está rodando como executável ou script
    if getattr(sys, 'frozen', False):
        # Executável PyInstaller
        base_path = os.path.dirname(sys.executable)
    else:
        # Script Python normal
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    arquivo_path = os.path.join(base_path, arquivo)
    
    if not os.path.exists(arquivo_path):
        return jsonify({
            'success': False, 
            'message': f'Arquivo não encontrado em: {arquivo_path}'
        }), 404
    
    try:
        return send_file(
            arquivo_path, 
            as_attachment=True, 
            download_name='dados_simulados_br.csv',
            mimetype='text/csv'
        )
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Erro ao enviar arquivo: {str(e)}'
        }), 500

def start_server():
    """Inicia o servidor Flask em uma thread separada"""
    app.run(debug=False, port=5000, use_reloader=False)

if __name__ == '__main__':
    # Inicia o servidor Flask em uma thread
    server_thread = Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Cria a janela do aplicativo
    webview.create_window(
        '📊 Calendário List - Sistema de Simulação',
        'http://127.0.0.1:5000',
        width=1200,
        height=800,
        resizable=True,
        fullscreen=False,
        min_size=(800, 600),
        confirm_close=True
    )
    
    # Inicia a GUI (bloqueia até a janela ser fechada)
    webview.start()