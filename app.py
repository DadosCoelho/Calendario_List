from flask import Flask, render_template, jsonify, send_file
import os
import sys
import webbrowser
from threading import Timer
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

# Função para capturar saída do print
class OutputCapture:
    def __init__(self):
        self.output = []
    
    def write(self, text):
        if text.strip():
            self.output.append(text)
    
    def flush(self):
        pass
    
    def get_output(self):
        return '\n'.join(self.output)

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
        # Captura a saída do print
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
    if not os.path.exists(arquivo):
        return jsonify({'success': False, 'message': 'Arquivo não encontrado!'})
    
    return send_file(arquivo, as_attachment=True, download_name='dados_simulados_br.csv')

def open_browser():
    # Abre em uma nova janela separada do navegador
    webbrowser.open('http://127.0.0.1:5000/', new=1)

if __name__ == '__main__':
    # Abre o navegador após 1 segundo
    Timer(1, open_browser).start()
    
    # Inicia o servidor Flask
    app.run(debug=False, port=5000)