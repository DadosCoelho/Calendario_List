# relatorio_listas_por_intervalo.py

import csv
from collections import Counter
from config_tabelas import distribuicao_listas  # <-- usa FAIXAS de listas

def gerar_relatorio_listas_por_intervalo(arquivo_csv):
    print("\nRELATÓRIO DE LISTAS POR INTERVALO AGRUPADO POR FAIXAS\n")

    faixas = list(distribuicao_listas.keys())
    contagem_faixas = {faixa: 0 for faixa in faixas}
    total_intervalos = 0

    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            listas_str = row["Listas"].strip()
            if "Nenhum" in listas_str or "Sem geração" in listas_str or not listas_str:
                continue

            qtd_listas = len([p for p in listas_str.split(";") if p.strip()])
            total_intervalos += 1

            # identifica faixa correspondente
            for faixa in faixas:
                ini, fim = faixa
                if ini <= qtd_listas <= fim:
                    contagem_faixas[faixa] += 1
                    break

    if total_intervalos == 0:
        print("Nenhum intervalo válido encontrado.")
        return

    print(f"{'Faixa':<20} {'Intervalos':<15} {'Percentual'}")
    print("-" * 55)

    for faixa in faixas:
        ini, fim = faixa
        qtd = contagem_faixas[faixa]
        perc = (qtd / total_intervalos) * 100
        print(f"{f'{ini} a {fim}':<20} {qtd:<15} {perc:>7.2f}%")

    print(f"\nTotal de intervalos analisados: {total_intervalos}")
