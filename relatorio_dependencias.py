import csv
from collections import defaultdict
from config_tabelas import tabela_numeros

def gerar_relatorio_dependencias(arquivo_csv):
    print("\n🔗 RELATÓRIO DE DEPENDÊNCIAS ENTRE NÚMEROS\n")

    # --- Contadores ---
    ativacoes = defaultdict(int)
    total_ocorrencias = defaultdict(int)

    # --- Lê o CSV e verifica dependências ativadas ---
    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            listas = row["Listas"]
            if "Nenhum" in listas or not listas.strip():
                continue

            partes = listas.split(";")
            for parte in partes:
                numeros = [int(x) for x in parte.strip(" []").split(",") if x.strip().isdigit()]

                for num in numeros:
                    num_str = str(num)
                    info = tabela_numeros.get(num_str, {})
                    deps = info.get("dependencias", {})
                    if not deps:
                        continue

                    total_ocorrencias[num] += 1
                    # Verifica se algum número dependente também saiu
                    for dep_num in deps.keys():
                        if int(dep_num) in numeros:
                            ativacoes[num] += 1
                            break  # basta uma ativação por lista

    # --- Exibir relatório ---
    print(f"{'Número':<10} {'Ocorrências':<12} {'Ativações':<12} {'Aproveitamento':<15}")
    print("-" * 55)

    for num in sorted(total_ocorrencias.keys()):
        total = total_ocorrencias[num]
        ativ = ativacoes.get(num, 0)
        aproveitamento = (ativ / total * 100) if total > 0 else 0
        print(f"{num:<10} {total:<12} {ativ:<12} {aproveitamento:>10.2f}%")

    print("\n📈 Total de números com dependências aproveitadas:", len(ativacoes))
