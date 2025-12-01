## 📝 README: Meu Primeiro Pipeline ETL (Recomendação de Vagas)

---

## 🚀 O que é este Projeto?

Este projeto é um **Pipeline ETL** (Extração, Transformação e Carregamento) que criei para praticar Engenharia de Dados com Python e a biblioteca Pandas.

O objetivo é simular um sistema que **recomenda vagas de emprego** para usuários com base nas habilidades que eles possuem.

### 🌟 Destaques do Projeto

* **Extração Simples:** Lê dados de usuários e vagas em formato CSV.
* **Inteligência:** O sistema calcula a compatibilidade entre as *skills* do usuário e os requisitos da vaga.
* **Organização:** O código é dividido em módulos (`extract`, `transform`, `load`) para ser fácil de entender e manter.
* **Reaproveitamento:** Garante que a mesma recomendação não seja enviada duas vezes ao mesmo usuário (Idempotência).

---

## ⚙️ Estrutura do Projeto

A estrutura foi organizada da seguinte forma:

ETL-RECOMENDACAO-VAGAS/ ├── data/ │ ├── jobs.csv # Vagas disponíveis (Entrada) │ ├── user_news.csv # Histórico de Recomendações (Saída) │ └── users.csv # Perfil dos Usuários (Entrada) └── src/ ├── config.py # Guarda configurações (Ex: nota mínima para recomendar) ├── extract.py # Lida com a leitura dos CSVs ├── load.py # Salva o resultado final no user_news.csv ├── transform.py # Contém a lógica de cálculo do score └── utils.py # Funções auxiliares (como normalizar as skills)


### 🔄 Como o Pipeline Funciona?

1.  **Extração:** O sistema lê as habilidades dos usuários e as habilidades requeridas pelas vagas.
2.  **Transformação:** Ele limpa as habilidades (ex: transforma "SQL" e "sql" em "sql") e usa a lógica de *scoring* para calcular quantos pontos cada usuário tem para cada vaga. 

[Image of a data pipeline diagram showing Extract, Transform, and Load steps, with the Transform step highlighting AI and GPT-4 integration]

3.  **Carregamento:** As recomendações mais relevantes são salvas no arquivo `user_news.csv` para uso futuro.

---

## 💻 Guia de Execução (Google Colab)

Para rodar este projeto, você precisa montar a mesma estrutura de pastas no ambiente do Colab e fazer o upload dos arquivos.

### 1. Preparação do Ambiente

Crie um novo Notebook e execute esta célula primeiro:

```python
# Célula 1: Configuração do Ambiente
import sys
import pandas as pd

# Criação das pastas 'data' e 'src'
!mkdir -p data
!mkdir -p src

# Adiciona a pasta 'src' ao caminho do Python para que as importações funcionem
if 'src' not in sys.path:
    sys.path.append('src')

print("Ambiente configurado. Agora, faça o upload dos seus arquivos.")
2. Upload
Use o painel de Arquivos (na lateral esquerda) para:

Subir seus arquivos da pasta src/ para a pasta src no Colab.

Subir seus arquivos users.csv e jobs.csv para a pasta data no Colab.

3. Execução
Crie uma nova célula no Colab e execute a função principal:

Python

# Célula 2: Execução do Pipeline
from src.config import Config
from src.pipeline import run_pipeline # Se sua função principal estiver em pipeline.py

# ... (Seu código completo deve estar no Notebook antes desta célula) ...

# Roda o pipeline e exibe as últimas recomendações
output_df = run_pipeline() 
print("\n--- Resultado do Carregamento (Últimas Mensagens) ---")
print(output_df.tail(10))
🧑‍🎓 Conclusão e Próximos Passos
Ao desenvolver este projeto, eu me concentrei em construir um pipeline que fosse claro, funcional e que usasse boas práticas, mesmo sendo iniciante. Estruturei o código em módulos e garanto que o sistema é robusto o suficiente para não duplicar dados e lidar com a entrada de forma limpa.

Eu transformei um desafio de código em um projeto prático de portfólio que demonstra meu entendimento do ciclo ETL e minha habilidade de criar soluções modulares.

🔗 Links
Notebook Colab: https://colab.research.google.com/drive/16i64d_kGY7PkzT8uwhz4y_nA67cVg_BU

Repositório GitHub: https://github.com/lucasavmiranda/etl-recomendacao-vagas