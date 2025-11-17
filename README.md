# 📊 Sistema de Simulação de Listas e Números  
Simulador completo com geração dinâmica de faixas, relatórios agrupados e parâmetros totalmente configuráveis.

Este projeto gera simulações baseadas em probabilidades, horários, dependências e faixas dinâmicas para **quantidade de listas** e **quantidade de números por lista**, além de diversos relatórios analíticos.

---

## 🚀 Funcionalidades

- Geração de dados simulados com:
  - Distribuição dinâmica de listas
  - Distribuição dinâmica de números
  - Estações e eventos com multiplicadores
  - Horários com chance variável
- Relatórios completos:
  - Ranking de números por mês
  - Aproveitamento de dependências
  - Tamanho das listas por faixas configuradas
  - Quantidade de listas por intervalo (10 min)
  - Sorteios por horário (pick)
- Parametrização totalmente flexível via `config_tabelas.py`

---

## ⚙️ Estrutura Geral do Projeto

``config_tabelas.py``  
Armazena todas as configurações do sistema:

- Calendário
- Horários
- Distribuições dinâmicas
- Multiplicadores por estação/evento
- Probabilidades base e dependências

``simulador.py``  
Executa a simulação completa, gerando o arquivo `dados_simulados_br.csv`.

``menu_principal.py``  
Interface de terminal que acessa todas as funções.

``relatorios_*``  
Módulos que geram cada relatório.

---

## 📌 Parametrização de Faixas Dinâmicas

As distribuições são definidas assim:

``faixas_percentuais_listas = [0.50, 0.20, 0.15, 0.10, 0.05]``  
``distribuicao_lista_max = 50``

Esses valores geram automaticamente faixas assim:

``1 a 25``  
``26 a 35``  
``36 a 42``  
``43 a 47``  
``48 a 50``

As faixas são calculadas pela função:

``gerar_distribuicao_dinamica(maximo, percentuais)``

Que garante:

- Nenhuma faixa residual extra
- A última faixa sempre ajustada ao máximo exato
- Número de faixas = número de percentuais

---

## ▶️ Como executar

1. Ative seu ambiente virtual:
``venv\Scripts\activate``

2. Rode o menu:
``python menu_principal.py``

3. Escolha uma das opções:
- **1** – Gerar simulação  
- **2** – Relatório top números mensais  
- **3** – Dependências  
- **4** – Tamanho das listas por faixas  
- **5** – Quantidade de listas por intervalo (faixas)  
- **6** – Relatório pick  

---

## 📁 Saída da Simulação

O gerador cria automaticamente:

``dados_simulados_br.csv``

Com as colunas:

- Data  
- Hora  
- Chance  
- Listas  

---

## 🔧 Ajustando a Distribuição

Para mudar as faixas, edite:

``config_tabelas.py``

Exemplo:

``distribuicao_numeros_max = 40``  
``faixas_percentuais_numeros = [0.40, 0.25, 0.15, 0.12, 0.08]``

---

## 🧠 Exemplo de Relatório Gerado (resumido)

``Faixa      Listas    Percentual``  
``1 a 16     65649     39.84%``  
``17 a 26    41341     25.09%``  
``27 a 32    24791     15.04%``  

---

## 🤝 Contribuição

Pull requests são bem-vindos!  
Para publicar suas alterações:

1. Adicione:
``git add .``

2. Commit:
``git commit -m "Atualiza parâmetros e faixas dinâmicas"``

3. Envie:
``git push``

---

## 📜 Licença

Projeto privado. Não distribuir sem autorização.
