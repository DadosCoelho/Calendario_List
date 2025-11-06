import random
import time
from datetime import datetime, timedelta

def gerar_dados_simulados():
    # começa em 08:00 (data arbitrária)
    hora_simulada = datetime.strptime("08:00", "%H:%M")
    passos_totais = 48  # 48 segundos / passos (8h úteis × 6s por hora => 48s)
    
    try:
        for passo in range(1, passos_totais + 1):
            # Formata HH:MM para exibição
            hora_label = hora_simulada.strftime("%H:%M")
            
            # 25% de chance de gerar o dado
            if random.random() < 0.25:
                quantidade = random.randint(1, 5)
                numeros = random.sample(range(1, 51), quantidade)
                print(f"[{hora_label}] Segundo {passo:02d}: {numeros}")
            else:
                print(f"[{hora_label}] Segundo {passo:02d}: (sem dado gerado)")
            
            # Avança 10 minutos na simulação (1 segundo real = 10 minutos simulados)
            hora_simulada += timedelta(minutes=10)
            
            # Se chegarmos a 12:00 (início do almoço), pular para 14:00
            # (no fluxo com passos de 10 minutos isso ocorrerá exatamente em 12:00)
            if hora_simulada.hour == 12 and hora_simulada.minute == 0:
                hora_simulada = hora_simulada.replace(hour=14, minute=0)
            
            time.sleep(1)  # espera 1 segundo real entre passos

        print("\nSimulação encerrada — Dia comercial completo (08:00 → 17:50).")

    except KeyboardInterrupt:
        print("\nSimulação interrompida pelo usuário.")

if __name__ == "__main__":
    gerar_dados_simulados()
