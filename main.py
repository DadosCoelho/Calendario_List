import json
import random
import time
from datetime import datetime, timedelta

# --- tabela de horários de pico (pode vir de um arquivo JSON) ---
horarios_pick = {
    "08:00-09:00": 0.20,
    "09:00-11:00": 0.35,
    "11:00-12:00": 0.25,
    "14:00-15:00": 0.30,
    "15:00-17:00": 0.45,
    "17:00-18:00": 0.25
}

def get_chance(hora):
    """Retorna a chance de gerar dado com base no horário simulando os picos."""
    for faixa, chance in horarios_pick.items():
        inicio, fim = faixa.split('-')
        hora_inicio = datetime.strptime(inicio, "%H:%M").time()
        hora_fim = datetime.strptime(fim, "%H:%M").time()
        if hora_inicio <= hora < hora_fim:
            return chance
    return 0.0

def gerar_dados_simulados():
    hora_simulada = datetime.strptime("08:00", "%H:%M")
    passos_totais = 48  # 48 passos = 8 horas úteis
    try:
        for passo in range(1, passos_totais + 1):
            hora_label = hora_simulada.strftime("%H:%M")
            chance = get_chance(hora_simulada.time())

            # Decide se gera dado com base na chance variável
            if random.random() < chance:
                quantidade = random.randint(1, 5)
                numeros = random.sample(range(1, 51), quantidade)
                print(f"[{hora_label}] ({chance*100:.0f}%) Segundo {passo:02d}: {numeros}")
            else:
                print(f"[{hora_label}] ({chance*100:.0f}%) Segundo {passo:02d}: (sem dado gerado)")

            # Avança 10 minutos simulados por segundo real
            hora_simulada += timedelta(minutes=10)
            if hora_simulada.hour == 12 and hora_simulada.minute == 0:
                hora_simulada = hora_simulada.replace(hour=14, minute=0)
            
            time.sleep(1)

        print("\nSimulação encerrada — Dia comercial completo (08:00 → 17:50).")
    except KeyboardInterrupt:
        print("\nSimulação interrompida pelo usuário.")

if __name__ == "__main__":
    gerar_dados_simulados()
