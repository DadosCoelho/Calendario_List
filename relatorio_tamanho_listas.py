# relatorio_tamanho_listas.py

import csv
from collections import Counter

def gerar_relatorio_tamanho_listas(arquivo_csv):
    print("\nRELATÓRIO DE TAMANHO DAS LISTAS GERADAS\n")

    contador_tamanhos = Counter()
    total_listas = 0

    # --- Lê o CSV e conta quantos números há em cada lista ---
    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            listas = row["Listas"]
            if "Nenhum" in listas or not listas.strip():
                continue

            partes = listas.split(";")
            for parte in partes:
                numeros = [x.strip() for x in parte.strip(" []").split(",") if x.strip().isdigit()]
                tamanho = len(numeros)
                if tamanho > 0:
                    contador_tamanhos[tamanho] += 1
                    total_listas += 1

    if total_listas == 0:
        print("Nenhuma lista válida encontrada no arquivo.")
        return

    print(f"{'Qtd. de números':<20} {'Listas':<10} {'Percentual':<10}")
    print("-" * 40)

    for tamanho in sorted(contador_tamanhos.keys()):
        qtd = contador_tamanhos[tamanho]
        perc = (qtd / total_listas) * 100
        print(f"{tamanho:<20} {qtd:<10} {perc:>7.2f}%")

    print(f"\nTotal de listas analisadas: {total_listas}")
