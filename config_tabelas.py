# config_tabelas.py

# ---- Configuração de calendário e horários ----
config_calendario = {
    "ano_inicial": 2000,  # ano de início da simulação
    "dia_semana_inicial": "segunda-feira",  # força o ano a começar numa segunda-feira

    # quantidade de dias em cada mês (ano não bissexto)
    "dias_mes": [
        {"mes": 1, "dias": 31},
        {"mes": 2, "dias": 28},
        {"mes": 3, "dias": 31},
        {"mes": 4, "dias": 30},
        {"mes": 5, "dias": 31},
        {"mes": 6, "dias": 30},
        {"mes": 7, "dias": 31},
        {"mes": 8, "dias": 31},
        {"mes": 9, "dias": 30},
        {"mes": 10, "dias": 31},
        {"mes": 11, "dias": 30},
        {"mes": 12, "dias": 31},
    ],

    # definição dos dias da semana
    "dia_util": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"],
    "meio_periodo": ["sábado"],
    "folga": ["domingo"],

    # horários padrão de funcionamento
    "horarios_dia_util": [("08:00", "12:00"), ("14:00", "18:00")],
    "horarios_meio_periodo": [("08:00", "12:00")],

    # feriados nacionais fixos
    "feriados": [
        {"data": "01/01", "descricao": "Confraternização Universal"},
        {"data": "21/04", "descricao": "Tiradentes"},
        {"data": "01/05", "descricao": "Dia do Trabalhador"},
        {"data": "07/09", "descricao": "Independência do Brasil"},
        {"data": "12/10", "descricao": "Nossa Senhora Aparecida"},
        {"data": "02/11", "descricao": "Finados"},
        {"data": "15/11", "descricao": "Proclamação da República"},
        {"data": "25/12", "descricao": "Natal"},
    ]
}

# ---- Tabelas de configuração ----
horarios_pick = {
    "08:00-09:00": 0.20,
    "09:00-11:00": 0.35,
    "11:00-12:00": 0.25,
    "14:00-15:00": 0.50,
    "15:00-17:00": 0.85,
    "17:00-18:00": 0.65
}

# ---- Distribuições ----
distribuicao_listas = {1: 0.50, 2: 0.20, 3: 0.15, 4: 0.10, 5: 0.05}
distribuicao_numeros = {1: 0.40, 2: 0.25, 3: 0.15, 4: 0.12, 5: 0.08}

# ---- Tipos combinados (estações e eventos) ----
class_tipo = {
    # ---- ESTAÇÕES ----
    1: {"descricao": "Verão", "tipo": "estação", "meses": [1, 2, 3], "mult": 3.5},
    2: {"descricao": "Outono", "tipo": "estação", "meses": [4, 5, 6], "mult": 3.2},
    3: {"descricao": "Inverno", "tipo": "estação", "meses": [7, 8, 9], "mult": 3.8},
    4: {"descricao": "Primavera", "tipo": "estação", "meses": [10, 11, 12], "mult": 3.4},

    # ---- EVENTOS ----
    5: {"descricao": "Férias de Verão", "tipo": "evento", "meses": [1], "mult": 3.5},
    6: {"descricao": "Carnaval", "tipo": "evento", "meses": [2], "mult": 3.5},
    7: {"descricao": "Semana Santa e Páscoa", "tipo": "evento", "meses": [3], "mult": 3.5},
    8: {"descricao": "Dia das Mães", "tipo": "evento", "meses": [5], "mult": 3.2},
    9: {"descricao": "Festa Junina", "tipo": "evento", "meses": [6], "mult": 3.3},
    10: {"descricao": "Dia dos Pais", "tipo": "evento", "meses": [7], "mult": 3.2},
    11: {"descricao": "Dia das Crianças", "tipo": "evento", "meses": [10], "mult": 3.5},
    12: {"descricao": "Halloween", "tipo": "evento", "meses": [10], "mult": 3.0},
    13: {"descricao": "Natal", "tipo": "evento", "meses": [12], "mult": 3.8},
    14: {"descricao": "Réveillon", "tipo": "evento", "meses": [12], "mult": 4.0},
}


# ---- Probabilidades base (com tipos combinados) ----
tabela_numeros = {
    "1": {"base_chance": 1.50, "dependencias": {"2": 17.00}, "tipo": [1, 5]},
    "2": {"base_chance": 1.50, "dependencias": {"1": 15.00}, "tipo": [1, 5]},
    "3": {"base_chance": 1.20, "dependencias": {"4": 16.00}, "tipo": [1, 6]},
    "4": {"base_chance": 1.00, "dependencias": {"3": 14.00}, "tipo": [1, 6]},
    "5": {"base_chance": 1.00, "dependencias": {"8": 19.00}, "tipo": [1, 7]},
    "6": {"base_chance": 1.20, "dependencias": {"8": 18.00}, "tipo": [1, 7]},
    "7": {"base_chance": 1.10, "dependencias": {"8": 17.00}, "tipo": [1, 7]},
    "8": {"base_chance": 2.00, "dependencias": {"5": 14.00, "6": 14.00, "7": 14.00}, "tipo": [1, 7]},
    "9": {"base_chance": 2.50, "dependencias": {}, "tipo": [1]},
    "10": {"base_chance": 0.80, "dependencias": {"14": 20.00}, "tipo": [2]},
    "11": {"base_chance": 1.20, "dependencias": {"14": 19.00}, "tipo": [2]},
    "12": {"base_chance": 1.00, "dependencias": {"14": 18.00}, "tipo": [2]},
    "13": {"base_chance": 0.90, "dependencias": {"14": 17.00}, "tipo": [2]},
    "14": {"base_chance": 1.80, "dependencias": {"11": 14.00}, "tipo": [2]},
    "15": {"base_chance": 1.30, "dependencias": {"16": 15.00}, "tipo": [2, 8]},
    "16": {"base_chance": 1.60, "dependencias": {"15": 15.00}, "tipo": [2, 8]},
    "17": {"base_chance": 2.20, "dependencias": {"18": 18.00}, "tipo": [2, 9]},
    "18": {"base_chance": 2.00, "dependencias": {"17": 17.00}, "tipo": [2, 9]},
    "19": {"base_chance": 1.20, "dependencias": {}, "tipo": [2]},
    "20": {"base_chance": 0.80, "dependencias": {}, "tipo": [2]},
    "21": {"base_chance": 1.00, "dependencias": {}, "tipo": [2]},
    "22": {"base_chance": 0.90, "dependencias": {}, "tipo": [2]},
    "23": {"base_chance": 1.30, "dependencias": {}, "tipo": [2]},
    "24": {"base_chance": 1.00, "dependencias": {}, "tipo": [2]},
    "25": {"base_chance": 0.90, "dependencias": {}, "tipo": [2]},
    "26": {"base_chance": 0.80, "dependencias": {}, "tipo": [2]},
    "27": {"base_chance": 0.80, "dependencias": {}, "tipo": [3]},
    "28": {"base_chance": 1.60, "dependencias": {"29": 16.00}, "tipo": [3, 10]},
    "29": {"base_chance": 2.20, "dependencias": {"28": 16.00, "30": 15.00}, "tipo": [3, 10]},
    "30": {"base_chance": 2.40, "dependencias": {"29": 14.00}, "tipo": [3, 10]},
    "31": {"base_chance": 0.90, "dependencias": {}, "tipo": [3]},
    "32": {"base_chance": 0.80, "dependencias": {}, "tipo": [3]},
    "33": {"base_chance": 1.30, "dependencias": {}, "tipo": [3]},
    "34": {"base_chance": 1.00, "dependencias": {}, "tipo": [3]},
    "35": {"base_chance": 0.90, "dependencias": {}, "tipo": [3]},
    "36": {"base_chance": 1.60, "dependencias": {"37": 16.00}, "tipo": [3, 10]},
    "37": {"base_chance": 2.20, "dependencias": {"36": 14.00}, "tipo": [3, 10]},
    "38": {"base_chance": 0.90, "dependencias": {}, "tipo": [3, 10]},
    "39": {"base_chance": 1.00, "dependencias": {}, "tipo": [4]},
    "40": {"base_chance": 0.80, "dependencias": {}, "tipo": [4]},
    "41": {"base_chance": 2.00, "dependencias": {"42": 15.00}, "tipo": [4, 11]},
    "42": {"base_chance": 0.90, "dependencias": {"41": 14.00}, "tipo": [4, 11]},
    "43": {"base_chance": 1.30, "dependencias": {}, "tipo": [4]},
    "44": {"base_chance": 1.00, "dependencias": {}, "tipo": [4]},
    "45": {"base_chance": 1.00, "dependencias": {}, "tipo": [4, 12]},
    "46": {"base_chance": 1.40, "dependencias": {"47": 15.00}, "tipo": [4, 13]},
    "47": {"base_chance": 1.60, "dependencias": {"46": 15.00}, "tipo": [4, 13]},
    "48": {"base_chance": 0.90, "dependencias": {}, "tipo": [4, 12]},
    "49": {"base_chance": 2.00, "dependencias": {"50": 14.00}, "tipo": [4, 14]},
    "50": {"base_chance": 0.90, "dependencias": {"49": 15.00}, "tipo": [4, 14]},
}
