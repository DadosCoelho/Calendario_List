# relatorio_sorteios_pick.py

import csv
from datetime import datetime
from collections import Counter
from config_tabelas import horarios_pick


def gerar_relatorio_sorteios_pick(arquivo_csv):
    print("\nRELATÓRIO DE SORTEIOS POR HORÁRIOS PICK\n")

    contador_sorteados = Counter()
    contador_totais = Counter()

    # Converter horários_pick em faixas de tempo
    faixas_horario = []
    for faixa in horarios_pick.keys():
        inicio, fim = faixa.split("-")
        h_ini = datetime.strptime(inicio, "%H:%M").time()
        h_fim = datetime.strptime(fim, "%H:%M").time()
        faixas_horario.append((faixa, h_ini, h_fim))

    # Ler arquivo CSV e contar intervalos sorteados e totais
    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            hora_txt = row["Hora"].strip()
            listas_txt = row["Listas"].strip()

            try:
                hora_atual = datetime.strptime(hora_txt, "%H:%M").time()
            except ValueError:
                continue

            for faixa, h_ini, h_fim in faixas_horario:
                if h_ini <= hora_atual < h_fim:
                    contador_totais[faixa] += 1  # conta todos os intervalos (com e sem sorteio)
                    if "Nenhum" not in listas_txt and "Sem geração" not in listas_txt and listas_txt:
                        contador_sorteados[faixa] += 1  # conta só os sorteados
                    break

    print(f"{'Faixa Horária':<15} {'Qtd. de Sorteios':<20} {'Qtd. de Intervalos':<20} {'Percentual':<10}")
    print("-" * 70)

    for faixa in horarios_pick.keys():
        qtd_sorteios = contador_sorteados[faixa]
        qtd_intervalos = contador_totais[faixa]
        perc = (qtd_sorteios / qtd_intervalos * 100) if qtd_intervalos > 0 else 0
        print(f"{faixa:<15} {qtd_sorteios:<20} {qtd_intervalos:<20} {perc:>7.2f}%")

    total_sorteios = sum(contador_sorteados.values())
    total_intervalos = sum(contador_totais.values())
    perc_total = (total_sorteios / total_intervalos * 100) if total_intervalos > 0 else 0

    print("-" * 70)
    print(f"{'TOTAL':<15} {total_sorteios:<20} {total_intervalos:<20} {perc_total:>7.2f}%\n")
