# menu_principal.py

import os
from config_tabelas import tabela_numeros
from simulador import gerar_dados_simulados
from relatorio_top_mensal import gerar_relatorio_top_mensal
from relatorio_dependencias import gerar_relatorio_dependencias

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gerar simulação")
        print("2. Relatório top números mensais")
        print("3. Relatório aproveitamento dependências")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            gerar_dados_simulados(tabela_numeros)
            print("Simulação concluída!")
        elif opcao == "2":
            arquivo = "dados_simulados_br.csv"
            if not os.path.exists(arquivo):
                print("\nO arquivo 'dados_simulados_br.csv' não foi encontrado!")
            else:
                gerar_relatorio_top_mensal(arquivo, tabela_numeros)
            input("\nPressione ENTER para voltar...")
        elif opcao == "3":
            arquivo = "dados_simulados_br.csv"
            if not os.path.exists(arquivo):
                print("\nO arquivo 'dados_simulados_br.csv' não foi encontrado!")
            else:
                gerar_relatorio_dependencias(arquivo)
            input("\nPressione ENTER para voltar...")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
