import json
import random
import time
from datetime import datetime, timedelta

# ---- Tabelas de configuração ----
horarios_pick = {
    "08:00-09:00": 0.20,
    "09:00-11:00": 0.35,
    "11:00-12:00": 0.25,
    "14:00-15:00": 0.50,
    "15:00-17:00": 0.85,
    "17:00-18:00": 0.65
}

# tabela simplificada de probabilidades base por número
tabela_numeros = {
    "1": {"base_chance": 10.00, "dependencias": {"2": 10.00}},
    "2": {"base_chance": 0.25, "dependencias": {}},
    "3": {"base_chance": 0.20, "dependencias": {"4": 0.80}},
    "4": {"base_chance": 0.15, "dependencias": {}},
    "5": {"base_chance": 0.10, "dependencias": {"8": 0.80}},
    "6": {"base_chance": 0.30, "dependencias": {"8": 0.60}},
    "7": {"base_chance": 0.20, "dependencias": {"8": 0.40}},
    "8": {"base_chance": 0.40, "dependencias": {}},
    "9": {"base_chance": 0.60, "dependencias": {}},
    "10": {"base_chance": 0.10, "dependencias": {"14": 0.80}},
    "11": {"base_chance": 0.30, "dependencias": {"14": 0.80}},
    "12": {"base_chance": 0.20, "dependencias": {"14": 0.80}},
    "13": {"base_chance": 0.10, "dependencias": {"14": 0.80}},
    "14": {"base_chance": 0.20, "dependencias": {}},
    "15": {"base_chance": 0.30, "dependencias": {}},
    "16": {"base_chance": 0.40, "dependencias": {}},
    "17": {"base_chance": 0.60, "dependencias": {}},
    "18": {"base_chance": 0.50, "dependencias": {}},
    "19": {"base_chance": 0.30, "dependencias": {}},
    "20": {"base_chance": 0.10, "dependencias": {}},
    "21": {"base_chance": 0.20, "dependencias": {}},
    "22": {"base_chance": 0.10, "dependencias": {}},
    "23": {"base_chance": 0.30, "dependencias": {}},
    "24": {"base_chance": 0.20, "dependencias": {}},
    "25": {"base_chance": 0.10, "dependencias": {}},
    "26": {"base_chance": 0.10, "dependencias": {}},
    "27": {"base_chance": 0.10, "dependencias": {}},
    "28": {"base_chance": 0.40, "dependencias": {}},
    "29": {"base_chance": 0.50, "dependencias": {}},
    "30": {"base_chance": 0.60, "dependencias": {}},
    "31": {"base_chance": 0.10, "dependencias": {}},
    "32": {"base_chance": 0.10, "dependencias": {}},
    "33": {"base_chance": 0.30, "dependencias": {}},
    "34": {"base_chance": 0.20, "dependencias": {}},
    "35": {"base_chance": 0.10, "dependencias": {}},
    "36": {"base_chance": 0.40, "dependencias": {}},
    "37": {"base_chance": 0.60, "dependencias": {}},
    "38": {"base_chance": 0.10, "dependencias": {}},
    "39": {"base_chance": 0.20, "dependencias": {}},
    "40": {"base_chance": 0.10, "dependencias": {}},
    "41": {"base_chance": 0.50, "dependencias": {}},
    "42": {"base_chance": 0.10, "dependencias": {}},
    "43": {"base_chance": 0.30, "dependencias": {}},
    "44": {"base_chance": 0.20, "dependencias": {}},
    "45": {"base_chance": 0.20, "dependencias": {}},
    "46": {"base_chance": 0.30, "dependencias": {}},
    "47": {"base_chance": 0.40, "dependencias": {}},
    "48": {"base_chance": 0.10, "dependencias": {}},
    "49": {"base_chance": 0.50, "dependencias": {}},
    "50": {"base_chance": 0.10, "dependencias": {}}
}

# Probabilidades para número de listas geradas (1 a 5)
distribuicao_listas = {
    1: 0.50,
    2: 0.20,
    3: 0.15,
    4: 0.10,
    5: 0.05
}


# ---- Funções auxiliares ----
def get_chance_por_hora(hora):
    for faixa, chance in horarios_pick.items():
        inicio, fim = faixa.split('-')
        hora_inicio = datetime.strptime(inicio, "%H:%M").time()
        hora_fim = datetime.strptime(fim, "%H:%M").time()
        if hora_inicio <= hora < hora_fim:
            return chance
    return 0.0


def sortear_quantidade(probabilidades):
    """Sorteia uma quantidade (1 a 5) com base na distribuição fornecida."""
    opcoes = list(probabilidades.keys())
    pesos = list(probabilidades.values())
    return random.choices(opcoes, weights=pesos, k=1)[0]


def gerar_numeros_dinamicos():
    numeros_disponiveis = list(tabela_numeros.keys())
    chances = {n: tabela_numeros[n]["base_chance"] for n in numeros_disponiveis}

    resultado = []
    qtd = sortear_quantidade(distribuicao_listas)  # <- mesma distribuição das listas

    for _ in range(qtd):
        total = sum(chances.values())
        if total == 0:
            break
        pesos_norm = [chances[n] / total for n in numeros_disponiveis]
        escolhido = random.choices(numeros_disponiveis, weights=pesos_norm, k=1)[0]
        resultado.append(int(escolhido))
        numeros_disponiveis.remove(escolhido)
        chances.pop(escolhido)

        # Ajusta dependências dinâmicas
        for num, novo_valor in tabela_numeros[escolhido]["dependencias"].items():
            if num in chances:
                chances[num] = novo_valor

    return sorted(resultado)


def gerar_dados_simulados():
    hora_simulada = datetime.strptime("08:00", "%H:%M")
    passos_totais = 48  # 48 passos = 8h úteis (10min cada)
    opcoes = list(distribuicao_listas.keys())
    pesos = list(distribuicao_listas.values())

    try:
        for _ in range(passos_totais):
            hora_label = hora_simulada.strftime("%H:%M")
            chance_hora = get_chance_por_hora(hora_simulada.time())

            if random.random() < chance_hora:
                qtd_listas = random.choices(opcoes, weights=pesos, k=1)[0]
                listas = [gerar_numeros_dinamicos() for _ in range(qtd_listas)]
                listas_formatadas = ", ".join(str(lst) for lst in listas)
                print(f"[{hora_label}] ({chance_hora*100:.0f}%): {listas_formatadas}")
            else:
                print(f"[{hora_label}] ({chance_hora*100:.0f}%): Nenhum dado gerado")

            hora_simulada += timedelta(minutes=10)
            if hora_simulada.hour == 12 and hora_simulada.minute == 0:
                hora_simulada = hora_simulada.replace(hour=14, minute=0)

            time.sleep(1)

        print("\nSimulação encerrada — Dia comercial completo (08:00 → 17:50).")

    except KeyboardInterrupt:
        print("\nSimulação interrompida pelo usuário.")


if __name__ == "__main__":
    gerar_dados_simulados()
