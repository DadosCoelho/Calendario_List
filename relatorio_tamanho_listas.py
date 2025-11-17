# relatorio_tamanho_listas.py

import csv
from collections import Counter
from config_tabelas import distribuicao_numeros  # <-- usa as FAIXAS reais

def gerar_relatorio_tamanho_listas(arquivo_csv):
    print("\nRELATÓRIO DE TAMANHO DAS LISTAS POR FAIXAS CONFIGURADAS\n")

    # cria contadores por faixa
    faixas = list(distribuicao_numeros.keys())
    contagem_faixas = {faixa: 0 for faixa in faixas}
    total_listas = 0

    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            listas = row["Listas"]
            if "Nenhum" in listas or not listas.strip():
                continue

            partes = listas.split(";")
            for parte in partes:
                numeros = [
                    x.strip()
                    for x in parte.strip(" []").split(",")
                    if x.strip().isdigit()
                ]
                tamanho = len(numeros)

                # encontra em qual faixa esse tamanho cai
                for faixa in faixas:
                    ini, fim = faixa
                    if ini <= tamanho <= fim:
                        contagem_faixas[faixa] += 1
                        break

                total_listas += 1

    if total_listas == 0:
        print("Nenhuma lista válida encontrada.")
        return

    print(f"{'Faixa':<20} {'Listas':<10} {'Percentual'}")
    print("-" * 50)

    for faixa in faixas:
        ini, fim = faixa
        qtd = contagem_faixas[faixa]
        perc = (qtd / total_listas) * 100
        print(f"{f'{ini} a {fim}':<20} {qtd:<10} {perc:>7.2f}%")

    print(f"\nTotal de listas analisadas: {total_listas}")
