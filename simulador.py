# simulador.py

import csv
import random
import time
from datetime import datetime, timedelta
from collections import Counter, defaultdict

# importa todas as tabelas do arquivo separado
from config_tabelas import (
    horarios_pick,
    class_tipo,
    tabela_numeros,
    distribuicao_listas,
    distribuicao_numeros,
)

# ---- Funções utilitárias ----
def get_chance_por_hora(hora):
    for faixa, chance in horarios_pick.items():
        inicio, fim = faixa.split("-")
        h_ini = datetime.strptime(inicio, "%H:%M").time()
        h_fim = datetime.strptime(fim, "%H:%M").time()
        if h_ini <= hora < h_fim:
            return chance
    return 0.0


def sortear_quantidade(probabilidades):
    opcoes, pesos = list(probabilidades.keys()), list(probabilidades.values())
    return random.choices(opcoes, weights=pesos, k=1)[0]


def gerar_numeros_dinamicos(mes_atual, tabela_numeros):
    """
    Calcula as chances com base no mês atual, combinando multiplicadores
    de todos os 'tipos' associados ao número (estações e eventos).
    """
    numeros_disponiveis = list(tabela_numeros.keys())
    chances = {}

    for n in numeros_disponiveis:
        base = tabela_numeros[n]["base_chance"]
        mult_total = 1.0

        # percorre todos os tipos (estações/eventos)
        for tipo_id in tabela_numeros[n]["tipo"]:
            tipo_info = class_tipo.get(tipo_id, {})
            if mes_atual in tipo_info.get("meses", []):
                mult_total *= tipo_info.get("mult", 1.0)

        chances[n] = base * mult_total

    resultado = []
    qtd = sortear_quantidade(distribuicao_numeros)

    for _ in range(qtd):
        total = sum(chances.values())
        if total == 0:
            break

        pesos_norm = [chances[n] / total for n in numeros_disponiveis]
        escolhido = random.choices(numeros_disponiveis, weights=pesos_norm, k=1)[0]
        resultado.append(int(escolhido))

        # Remove número escolhido e aplica dependências
        numeros_disponiveis.remove(escolhido)
        chances.pop(escolhido)

        for num, novo_valor in tabela_numeros[escolhido]["dependencias"].items():
            if num in chances:
                chances[num] = novo_valor

    return sorted(resultado)


# ---- Função principal ----
def gerar_dados_simulados(tabela_numeros):
    arquivo_csv = "dados_simulados_br.csv"
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Data", "Hora", "Chance", "Listas"])

        sorteios_totais = Counter()
        sorteios_mensais = defaultdict(Counter)
        total_listas = 0

        ano = 2000
        passos_por_dia = 48

        for mes in range(1, 13):
            for dia in range(1, 29):
                hora_simulada = datetime.strptime("08:00", "%H:%M")
                for _ in range(passos_por_dia):
                    hora_label = hora_simulada.strftime("%H:%M")
                    chance_hora = get_chance_por_hora(hora_simulada.time())

                    if random.random() < chance_hora:
                        qtd_listas = sortear_quantidade(distribuicao_listas)
                        listas = [gerar_numeros_dinamicos(mes, tabela_numeros) for _ in range(qtd_listas)]
                        listas_formatadas = "; ".join(str(lst) for lst in listas)
                        writer.writerow([f"{dia:02d}/{mes:02d}/{ano}", hora_label, f"{chance_hora*100:.0f}%", listas_formatadas])
                        total_listas += qtd_listas
                        for lst in listas:
                            sorteios_totais.update(lst)
                            sorteios_mensais[mes].update(lst)
                    else:
                        writer.writerow([f"{dia:02d}/{mes:02d}/{ano}", hora_label, f"{chance_hora*100:.0f}%", "Nenhum dado gerado"])

                    hora_simulada += timedelta(minutes=10)
                    if hora_simulada.hour == 12:
                        hora_simulada = hora_simulada.replace(hour=14, minute=0)

                time.sleep(0.01)

    print("\n✅ Simulação concluída e salva em 'dados_simulados_br.csv'.")
    return sorteios_mensais
