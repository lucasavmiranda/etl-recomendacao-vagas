import os

class Config:
    DATA_DIR = "data"
    USERS_CSV = os.path.join(DATA_DIR, "users.csv")
    JOBS_CSV = os.path.join(DATA_DIR, "jobs.csv")
    USER_NEWS_CSV = os.path.join(DATA_DIR, "user_news.csv")

    # Ícone público para o campo "icon" no CSV de saída
    ICON_URL = "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg"

    # Regras de pontuação
    SCORE_PER_SKILL = 1
    MIN_SCORE = 2        # mínimo de skills em comum para recomendar
    MAX_RECS_PER_USER = 2  # máximo de recomendações por usuário
