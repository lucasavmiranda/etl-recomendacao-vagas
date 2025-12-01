import os
import pandas as pd
from .utils import log, normalize_skills, validate_required_columns
from .config import Config

def extract_users(path: str = Config.USERS_CSV) -> pd.DataFrame:
    log(f"Lendo {path}")
    df = pd.read_csv(path)
    validate_required_columns(df, {"user_id", "name", "skills"}, "users.csv")
    df["skills_norm"] = df["skills"].apply(normalize_skills)
    return df

def extract_jobs(path: str = Config.JOBS_CSV) -> pd.DataFrame:
    log(f"Lendo {path}")
    df = pd.read_csv(path)
    validate_required_columns(df, {"job_id","title","company","required_skills","location","level"}, "jobs.csv")
    df["required_skills_norm"] = df["required_skills"].apply(normalize_skills)
    return df

def extract_user_news(path: str = Config.USER_NEWS_CSV) -> pd.DataFrame:
    log(f"Verificando saída {path}")
    if not os.path.exists(path):
        pd.DataFrame(columns=["user_id","news_id","icon","description","created_at"]).to_csv(path, index=False)
    return pd.read_csv(path)
