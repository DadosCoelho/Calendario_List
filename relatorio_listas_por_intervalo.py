# relatorio_listas_por_intervalo.py

import csv
from collections import Counter

def gerar_relatorio_listas_por_intervalo(arquivo_csv):
    print("\nRELATÓRIO DE QUANTIDADE DE LISTAS POR INTERVALO (10 min)\n")

    contador_intervalos = Counter()
    total_intervalos = 0

    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            listas_str = row["Listas"].strip()
            # Ignorar linhas sem geração
            if "Nenhum" in listas_str or "Sem geração" in listas_str or not listas_str:
                continue

            # Contar quantas listas existem neste intervalo
            partes = [p for p in listas_str.split(";") if p.strip()]
            qtd_listas = len(partes)

            # Garantir que esteja dentro do limite 1–5
            if 1 <= qtd_listas <= 5:
                contador_intervalos[qtd_listas] += 1
                total_intervalos += 1

    if total_intervalos == 0:
        print("Nenhum intervalo válido encontrado no arquivo.")
        return

    print(f"{'Qtd. de listas':<20} {'Qtd. de intervalos':<22} {'Percentual':<10}")
    print("-" * 60)

    for qtd_listas in range(1, 6):
        qtd_intervalos = contador_intervalos[qtd_listas]
        perc = (qtd_intervalos / total_intervalos) * 100
        print(f"{qtd_listas:<20} {qtd_intervalos:<22} {perc:>7.2f}%")

    print(f"\nTotal de intervalos analisados: {total_intervalos}")
