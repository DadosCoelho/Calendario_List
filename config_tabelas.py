# config_tabelas.py

# ---- Tabelas de configuração ----
horarios_pick = {
    "08:00-09:00": 0.20,
    "09:00-11:00": 0.35,
    "11:00-12:00": 0.25,
    "14:00-15:00": 0.50,
    "15:00-17:00": 0.85,
    "17:00-18:00": 0.65
}

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

# ---- Probabilidades base ----
tabela_numeros = {
    "1": {"base_chance": 4.50, "dependencias":  {"2": 17.00}, "classEstacao": 1, "classEvento": 3},
    "2": {"base_chance": 1.50, "dependencias":  {"1": 15.00}, "classEstacao": 1, "classEvento": 3},
    "3": {"base_chance": 1.20, "dependencias":  {"4": 16.00}, "classEstacao": 1, "classEvento": 2},
    "4": {"base_chance": 1.00, "dependencias":  {"3": 14.00}, "classEstacao": 1, "classEvento": 2},
    "5": {"base_chance": 1.00, "dependencias":  {"8": 19.00}, "classEstacao": 1, "classEvento": 1},
    "6": {"base_chance": 1.20, "dependencias":  {"8": 18.00}, "classEstacao": 1, "classEvento": 1},
    "7": {"base_chance": 1.10, "dependencias":  {"8": 17.00}, "classEstacao": 1, "classEvento": 1},
    "8": {"base_chance": 2.00, "dependencias":  {"5": 14.00, "6": 14.00, "7": 14.00}, "classEstacao": 1, "classEvento": 1},
    "9": {"base_chance": 2.50, "dependencias":  {}, "classEstacao": 1, "classEvento": 0},
    "10": {"base_chance": 0.80, "dependencias":  {"14": 20.00}, "classEstacao": 1, "classEvento": 0},
    "11": {"base_chance": 1.20, "dependencias":  {"14": 19.00}, "classEstacao": 1, "classEvento": 0},
    "12": {"base_chance": 1.00, "dependencias":  {"14": 18.00}, "classEstacao": 1, "classEvento": 0},
    "13": {"base_chance": 0.90, "dependencias":  {"14": 17.00}, "classEstacao": 1, "classEvento": 0},
    "14": {"base_chance": 1.80, "dependencias":  {"11": 14.00}, "classEstacao": 1, "classEvento": 0},
    "15": {"base_chance": 1.30, "dependencias":  {"16": 15.00}, "classEstacao": 2, "classEvento": 4},
    "16": {"base_chance": 1.60, "dependencias":  {"15": 15.00}, "classEstacao": 2, "classEvento": 4},
    "17": {"base_chance": 2.20, "dependencias":  {"18": 18.00}, "classEstacao": 2, "classEvento": 5},
    "18": {"base_chance": 2.00, "dependencias":  {"17": 17.00}, "classEstacao": 2, "classEvento": 5},
    "19": {"base_chance": 1.20, "dependencias":  {}, "classEstacao": 2, "classEvento": 4},
    "20": {"base_chance": 0.80, "dependencias":  {}, "classEstacao": 2, "classEvento": 5},
    "21": {"base_chance": 1.00, "dependencias":  {}, "classEstacao": 2, "classEvento": 0},
    "22": {"base_chance": 0.90, "dependencias":  {}, "classEstacao": 2, "classEvento": 0},
    "23": {"base_chance": 1.30, "dependencias":  {}, "classEstacao": 2, "classEvento": 0},
    "24": {"base_chance": 1.00, "dependencias":  {}, "classEstacao": 2, "classEvento": 0},
    "25": {"base_chance": 0.90, "dependencias":  {}, "classEstacao": 2, "classEvento": 0},
    "26": {"base_chance": 0.80, "dependencias":  {}, "classEstacao": 2, "classEvento": 0},
    "27": {"base_chance": 0.80, "dependencias":  {}, "classEstacao": 3, "classEvento": 0},
    "28": {"base_chance": 1.60, "dependencias":  {"29": 16.00}, "classEstacao": 3, "classEvento": 0},
    "29": {"base_chance": 2.20, "dependencias":  {"28": 16.00, "30": 15.00}, "classEstacao": 3, "classEvento": 0},
    "30": {"base_chance": 2.40, "dependencias":  {"29": 14.00}, "classEstacao": 3, "classEvento": 0},
    "31": {"base_chance": 0.90, "dependencias":  {}, "classEstacao": 3, "classEvento": 0},
    "32": {"base_chance": 0.80, "dependencias":  {}, "classEstacao": 3, "classEvento": 0},
    "33": {"base_chance": 1.30, "dependencias":  {}, "classEstacao": 3, "classEvento": 0},
    "34": {"base_chance": 1.00, "dependencias":  {}, "classEstacao": 3, "classEvento": 0},
    "35": {"base_chance": 0.90, "dependencias":  {}, "classEstacao": 3, "classEvento": 0},
    "36": {"base_chance": 1.60, "dependencias":  {"37": 16.00}, "classEstacao": 3, "classEvento": 6},
    "37": {"base_chance": 2.20, "dependencias":  {"36": 14.00}, "classEstacao": 3, "classEvento": 6},
    "38": {"base_chance": 0.90, "dependencias":  {}, "classEstacao": 3, "classEvento": 6},
    "39": {"base_chance": 1.00, "dependencias":  {}, "classEstacao": 4, "classEvento": 0},
    "40": {"base_chance": 0.80, "dependencias":  {}, "classEstacao": 4, "classEvento": 0},
    "41": {"base_chance": 2.00, "dependencias":  {"42": 15.00}, "classEstacao": 4, "classEvento": 7},
    "42": {"base_chance": 0.90, "dependencias":  {"41": 14.00}, "classEstacao": 4, "classEvento": 7},
    "43": {"base_chance": 1.30, "dependencias":  {}, "classEstacao": 4, "classEvento": 0},
    "44": {"base_chance": 1.00, "dependencias":  {}, "classEstacao": 4, "classEvento": 0},
    "45": {"base_chance": 1.00, "dependencias":  {}, "classEstacao": 4, "classEvento": 8},
    "46": {"base_chance": 1.40, "dependencias":  {"47": 15.00}, "classEstacao": 4, "classEvento": 10},
    "47": {"base_chance": 1.60, "dependencias":  {"46": 15.00}, "classEstacao": 4, "classEvento": 10},
    "48": {"base_chance": 0.90, "dependencias":  {}, "classEstacao": 4, "classEvento": 8},
    "49": {"base_chance": 2.00, "dependencias":  {"50": 14.00}, "classEstacao": 4, "classEvento": 9},
    "50": {"base_chance": 0.90, "dependencias":  {"49": 15.00}, "classEstacao": 4, "classEvento": 9}
}

# ---- Distribuições ----
distribuicao_listas = {1: 0.50, 2: 0.20, 3: 0.15, 4: 0.10, 5: 0.05}
distribuicao_numeros = {1: 0.40, 2: 0.25, 3: 0.15, 4: 0.12, 5: 0.08}
