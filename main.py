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

# ---- Classificações ----
class_estacao = {
    1: {"descricao": "Verão", "meses": [1, 2, 3]},
    2: {"descricao": "Outono", "meses": [4, 5, 6]},
    3: {"descricao": "Inverno", "meses": [7, 8, 9]},
    4: {"descricao": "Primavera", "meses": [10, 11, 12]}
}

class_evento = {
    1: {"descricao": "Férias de Verão", "meses": [1]},
    2: {"descricao": "Carnaval", "meses": [2]},
    3: {"descricao": "Semana Santa e Páscoa", "meses": [3]},
    4: {"descricao": "Dia das Mães", "meses": [5]},
    5: {"descricao": "Festa Junina", "meses": [6]},
    6: {"descricao": "Dia dos Pais", "meses": [7]},
    7: {"descricao": "Dia das Crianças / Nossa Senhora Aparecida", "meses": [10]},
    8: {"descricao": "Halloween", "meses": [10]},
    9: {"descricao": "Natal", "meses": [12]},
    10: {"descricao": "Réveillon", "meses": [12]}
}

# ---- Probabilidades base de números ----
tabela_numeros = {
    "1": {"base_chance": 4.50, "dependencias": {"2": 17.00}, "classEstacao": 1, "classEvento": 3},
    "2": {"base_chance": 1.50, "dependencias": {"1": 15.00}, "classEstacao": 1, "classEvento": 3},
    "3": {"base_chance": 1.20, "dependencias": {"4": 16.00}, "classEstacao": 1, "classEvento": 2},
    "4": {"base_chance": 1.00, "dependencias": {"3": 14.00}, "classEstacao": 1, "classEvento": 2},
    "5": {"base_chance": 1.00, "dependencias": {"8": 19.00}, "classEstacao": 1, "classEvento": 1},
    "6": {"base_chance": 1.20, "dependencias": {"8": 18.00}, "classEstacao": 1, "classEvento": 1},
    "7": {"base_chance": 1.10, "dependencias": {"8": 17.00}, "classEstacao": 1, "classEvento": 1},
    "8": {"base_chance": 2.00, "dependencias": {"5": 14.00, "6": 14.00, "7": 14.00}, "classEstacao": 1, "classEvento": 1},
    "9": {"base_chance": 2.50, "dependencias": {}, "classEstacao": 1, "classEvento": 0},
    "10": {"base_chance": 0.80, "dependencias": {"14": 20.00}, "classEstacao": 1, "classEvento": 0},
    "11": {"base_chance": 1.20, "dependencias": {"14": 19.00}, "classEstacao": 1, "classEvento": 0},
    "12": {"base_chance": 1.00, "dependencias": {"14": 18.00}, "classEstacao": 1, "classEvento": 0},
    "13": {"base_chance": 0.90, "dependencias": {"14": 17.00}, "classEstacao": 1, "classEvento": 0},
    "14": {"base_chance": 1.80, "dependencias": {"11": 14.00}, "classEstacao": 1, "classEvento": 0},
    "15": {"base_chance": 1.30, "dependencias": {"16": 15.00}, "classEstacao": 2, "classEvento": 4},
    "16": {"base_chance": 1.60, "dependencias": {"15": 15.00}, "classEstacao": 2, "classEvento": 4},
    "17": {"base_chance": 2.20, "dependencias": {"18": 18.00}, "classEstacao": 2, "classEvento": 5},
    "18": {"base_chance": 2.00, "dependencias": {"17": 17.00}, "classEstacao": 2, "classEvento": 5},
    "19": {"base_chance": 1.20, "dependencias": {}, "classEstacao": 2, "classEvento": 4},
    "20": {"base_chance": 0.80, "dependencias": {}, "classEstacao": 2, "classEvento": 5},
    "21": {"base_chance": 1.00, "dependencias": {}, "classEstacao": 2, "classEvento": 0},
    "22": {"base_chance": 0.90, "dependencias": {}, "classEstacao": 2, "classEvento": 0},
    "23": {"base_chance": 1.30, "dependencias": {}, "classEstacao": 2, "classEvento": 0},
    "24": {"base_chance": 1.00, "dependencias": {}, "classEstacao": 2, "classEvento": 0},
    "25": {"base_chance": 0.90, "dependencias": {}, "classEstacao": 2, "classEvento": 0},
    "26": {"base_chance": 0.80, "dependencias": {}, "classEstacao": 2, "classEvento": 0},
    "27": {"base_chance": 0.80, "dependencias": {}, "classEstacao": 3, "classEvento": 0},
    "28": {"base_chance": 1.60, "dependencias": {"29": 16.00}, "classEstacao": 3, "classEvento": 0},
    "29": {"base_chance": 2.20, "dependencias": {"28": 16.00, "30": 15.00}, "classEstacao": 3, "classEvento": 0},
    "30": {"base_chance": 2.40, "dependencias": {"29": 14.00}, "classEstacao": 3, "classEvento": 0},
    "31": {"base_chance": 0.90, "dependencias": {}, "classEstacao": 3, "classEvento": 0},
    "32": {"base_chance": 0.80, "dependencias": {}, "classEstacao": 3, "classEvento": 0},
    "33": {"base_chance": 1.30, "dependencias": {}, "classEstacao": 3, "classEvento": 0},
    "34": {"base_chance": 1.00, "dependencias": {}, "classEstacao": 3, "classEvento": 0},
    "35": {"base_chance": 0.90, "dependencias": {}, "classEstacao": 3, "classEvento": 0},
    "36": {"base_chance": 1.60, "dependencias": {"37": 16.00}, "classEstacao": 3, "classEvento": 6},
    "37": {"base_chance": 2.20, "dependencias": {"36": 14.00}, "classEstacao": 3, "classEvento": 6},
    "38": {"base_chance": 0.90, "dependencias": {}, "classEstacao": 3, "classEvento": 6},
    "39": {"base_chance": 1.00, "dependencias": {}, "classEstacao": 4, "classEvento": 0},
    "40": {"base_chance": 0.80, "dependencias": {}, "classEstacao": 4, "classEvento": 0},
    "41": {"base_chance": 2.00, "dependencias": {"42": 15.00}, "classEstacao": 4, "classEvento": 7},
    "42": {"base_chance": 0.90, "dependencias": {"41": 14.00}, "classEstacao": 4, "classEvento": 7},
    "43": {"base_chance": 1.30, "dependencias": {}, "classEstacao": 4, "classEvento": 0},
    "44": {"base_chance": 1.00, "dependencias": {}, "classEstacao": 4, "classEvento": 0},
    "45": {"base_chance": 1.00, "dependencias": {}, "classEstacao": 4, "classEvento": 8},
    "46": {"base_chance": 1.40, "dependencias": {"47": 15.00}, "classEstacao": 4, "classEvento": 10},
    "47": {"base_chance": 1.60, "dependencias": {"46": 15.00}, "classEstacao": 4, "classEvento": 10},
    "48": {"base_chance": 0.90, "dependencias": {}, "classEstacao": 4, "classEvento": 8},
    "49": {"base_chance": 2.00, "dependencias": {"50": 14.00}, "classEstacao": 4, "classEvento": 9},
    "50": {"base_chance": 0.90, "dependencias": {"49": 15.00}, "classEstacao": 4, "classEvento": 9}
}

# Probabilidades para número de listas geradas (1 a 5)
distribuicao_listas = {1: 0.50, 2: 0.20, 3: 0.15, 4: 0.10, 5: 0.05}


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
    opcoes = list(probabilidades.keys())
    pesos = list(probabilidades.values())
    return random.choices(opcoes, weights=pesos, k=1)[0]


def gerar_numeros_dinamicos(mes_atual):
    numeros_disponiveis = list(tabela_numeros.keys())
    chances = {}

    for n in numeros_disponiveis:
        base = tabela_numeros[n]["base_chance"]
        mult = 1.0

        # bônus de estação
        est = tabela_numeros[n]["classEstacao"]
        if mes_atual in class_estacao.get(est, {}).get("meses", []):
            mult *= 2.5

        # bônus de evento
        ev = tabela_numeros[n]["classEvento"]
        if mes_atual in class_evento.get(ev, {}).get("meses", []):
            mult *= 2.5

        chances[n] = base * mult

    resultado = []
    qtd = sortear_quantidade(distribuicao_listas)

    for _ in range(qtd):
        total = sum(chances.values())
        if total == 0:
            break
        pesos_norm = [chances[n] / total for n in numeros_disponiveis]
        escolhido = random.choices(numeros_disponiveis, weights=pesos_norm, k=1)[0]
        resultado.append(int(escolhido))
        numeros_disponiveis.remove(escolhido)
        chances.pop(escolhido)

        for num, novo_valor in tabela_numeros[escolhido]["dependencias"].items():
            if num in chances:
                chances[num] = novo_valor

    return sorted(resultado)


def gerar_dados_simulados():
    ano, mes, dia = 2000, 1, 1
    hora_simulada = datetime.strptime("08:00", "%H:%M")
    passos_por_dia = 48

    try:
        while mes <= 12:
            for dia in range(1, 29):
                print(f"\nData simulada: {dia:02d}/{mes:02d}/{ano}")
                hora_simulada = datetime.strptime("08:00", "%H:%M")

                for _ in range(passos_por_dia):
                    hora_label = hora_simulada.strftime("%H:%M")
                    chance_hora = get_chance_por_hora(hora_simulada.time())

                    if random.random() < chance_hora:
                        qtd_listas = sortear_quantidade(distribuicao_listas)
                        listas = [gerar_numeros_dinamicos(mes) for _ in range(qtd_listas)]
                        listas_formatadas = ", ".join(str(lst) for lst in listas)
                        print(f"[{hora_label}] ({chance_hora*100:.0f}%): {listas_formatadas}")
                    else:
                        print(f"[{hora_label}] ({chance_hora*100:.0f}%): Nenhum dado gerado")

                    hora_simulada += timedelta(minutes=10)
                    if hora_simulada.hour == 12 and hora_simulada.minute == 0:
                        hora_simulada = hora_simulada.replace(hour=14, minute=0)

                    time.sleep(0.2)

            mes += 1

        print("\nSimulação encerrada — Ano completo (2000).")

    except KeyboardInterrupt:
        print("\nSimulação interrompida pelo usuário.")


if __name__ == "__main__":
    gerar_dados_simulados()
