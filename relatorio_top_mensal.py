# relatorio_top_mensal.py

import csv
from collections import Counter, defaultdict
from config_tabelas import class_estacao, class_evento

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

            # ---- Cálculo de multiplicadores ----
            mult = 1.0
            desc_estacao = class_estacao.get(info.get("classEstacao"), {}).get("descricao", "N/A")
            desc_evento = class_evento.get(info.get("classEvento"), {}).get("descricao", "Nenhum")

            estacao_info = class_estacao.get(info.get("classEstacao"), {})
            if mes in estacao_info.get("meses", []):
                mult *= estacao_info.get("mult", 1.0)

            evento_info = class_evento.get(info.get("classEvento"), {})
            if mes in evento_info.get("meses", []):
                mult *= evento_info.get("mult", 1.0)

            chance_calculada = base * mult
            perc = (freq / total_mes * 100) if total_mes else 0

            # formatações visuais
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
                f"Mult. Est/Evento: x{mult_s} → Chance final: {chance_s}  | "
                f"Estação: {desc_estacao}, Evento: {desc_evento}"
            )
