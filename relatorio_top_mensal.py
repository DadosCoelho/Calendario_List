# relatorio_top_mensal.py

import csv
from collections import Counter, defaultdict
from config_tabelas import class_tipo  # agora usamos a tabela combinada

def gerar_relatorio_top_mensal(arquivo_csv, tabela_numeros):
    sorteios_mensais = defaultdict(Counter)

    # --- Lê o CSV e monta o contador por mês ---
    with open(arquivo_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            data = row["Data"]
            listas = row["Listas"]
            if "Nenhum" in listas or not listas.strip():
                continue

            mes = int(data.split("/")[1])
            partes = listas.split(";")
            for parte in partes:
                numeros = [int(x) for x in parte.strip(" []").split(",") if x.strip().isdigit()]
                sorteios_mensais[mes].update(numeros)

    # --- Gera relatório formatado ---
    print("\nRANKING DE NÚMEROS POR MÊS\n")

    for mes, contador in sorted(sorteios_mensais.items()):
        total_mes = sum(contador.values())
        print(f"\nMÊS {mes:02d} — Total de números sorteados: {total_mes}")

        mais_frequentes = contador.most_common(10)

        for i, (num, freq) in enumerate(mais_frequentes, start=1):
            num_str = str(num)
            info = tabela_numeros.get(num_str, {})
            base = info.get("base_chance", 1.0)

            # ---- Tipos atribuídos ao número (ex.: estação + evento) ----
            tipos_ids = info.get("tipo", []) or info.get("classTipo", []) or []
            # descrição completa dos tipos atribuídos (independente do mês)
            if tipos_ids:
                descricoes_tipos = [class_tipo.get(tid, {}).get("descricao", f"Tipo{tid}") for tid in tipos_ids]
                desc_tipo = ", ".join(descricoes_tipos)
            else:
                desc_tipo = "N/A"

            # ---- Cálculo do multiplicador somente para os tipos ATIVOS no mês ----
            mult = 1.0
            for tid in tipos_ids:
                tipo_info = class_tipo.get(tid, {})
                if mes in tipo_info.get("meses", []):
                    mult *= tipo_info.get("mult", 1.0)

            chance_calculada = base * mult
            perc = (freq / total_mes * 100) if total_mes else 0

            # ---- Formatações visuais (pt-BR: vírgula decimal) ----
            perc_s = f"{perc:5.2f}".replace(".", ",")
            ip, dp = perc_s.split(",")
            ip = ip.rjust(2, " ")
            perc_s = f"{ip},{dp}%"

            base_s = f"{base:.2f}".replace(".", ",")
            ip, dp = base_s.split(",")
            ip = ip.rjust(2, " ")
            base_s = f"{ip},{dp}"

            chance_s = f"{chance_calculada:5.2f}".replace(".", ",")
            ip, dp = chance_s.split(",")
            chance_s = f"{ip.rjust(2, ' ')},{dp}"

            mult_s = f"{mult:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").rjust(6, " ")

            print(
                f"{i:02d}º → Número {num:2d}: {freq:5d} vezes "
                f"({perc_s}) | Base: {base_s} | "
                f"Multiplicador Tipo: x{mult_s} → Chance final: {chance_s}  | "
                f"Tipo: {desc_tipo}"
            )
