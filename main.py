import random
import time
from datetime import datetime

def gerar_dados():
    segundo = 0
    try:
        while True:
            segundo += 1
            # 25% de chance de gerar o dado
            if random.random() < 0.25:
                quantidade = random.randint(1, 5)
                numeros = random.sample(range(1, 51), quantidade)
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Segundo {segundo:03d}: {numeros}")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Segundo {segundo:03d}: (sem dado gerado)")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")

if __name__ == "__main__":
    gerar_dados()
