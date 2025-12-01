# Arquivo: pipeline.py

import pandas as pd
import os
import sys

# Garante que a pasta src esteja no PATH para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importa as funções dos módulos em src/
from config import Config
from extract import extract_users, extract_jobs, extract_user_news
from transform import recommend_jobs_for_user, build_message
from load import append_news, save_news
from utils import log

# =========================
# Pipeline de Orquestração
# =========================

def run_pipeline():
    """
    Executa o ciclo completo de Extração, Transformação e Carregamento (ETL).
    """
    log("Início do Pipeline ETL")
    
    # 1. EXTRAÇÃO (Extract)
    try:
        users_df = extract_users(Config.USERS_CSV)
        jobs_df = extract_jobs(Config.JOBS_CSV)
        news_df = extract_user_news(Config.USER_NEWS_CSV)
    except FileNotFoundError as e:
        log(f"ERRO: Arquivo de dados não encontrado: {e.filename}. Certifique-se de que os CSVs estão na pasta 'data/'.")
        return pd.DataFrame() # Retorna DataFrame vazio em caso de erro

    # 2. TRANSFORMAÇÃO (Transform)
    total_msgs = 0
    for _, user in users_df.iterrows():
        recs = recommend_jobs_for_user(user, jobs_df)
        
        if not recs:
            # log(f"Sem recomendações para {user['name']}.") # Opcional: desativado para logs mais limpos
            continue
            
        for rec in recs:
            # Constrói a mensagem
            msg = build_message(user["name"], rec["job"], rec["score"], rec["matched_skills"])
            
            # 3. CARREGAMENTO (Load) - Usando a função append_news para garantir idempotência
            news_df = append_news(news_df, user["user_id"], msg, Config.ICON_URL)
            total_msgs += 1

    # 4. SALVAMENTO
    save_news(news_df, Config.USER_NEWS_CSV)
    
    log(f"ETL finalizado. Mensagens processadas (incluindo possíveis duplicadas que foram puladas): {total_msgs}")
    return news_df

# =========================
# Execução (Se rodado como script principal)
# =========================

if __name__ == "__main__":
    output_df = run_pipeline()
    print("\n--- Resultado do Carregamento (Últimas Mensagens) ---")
    if not output_df.empty:
        print(output_df.tail(10))
    else:
        print("Pipeline não produziu resultados.")