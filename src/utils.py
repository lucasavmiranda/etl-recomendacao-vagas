from datetime import datetime
import pandas as pd

def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")

def normalize_skills(text: str) -> list:
    if pd.isna(text) or str(text).strip() == "":
        return []
    return [s.strip().lower() for s in str(text).split(";") if s.strip()]

def validate_required_columns(df: pd.DataFrame, required: set, filename: str) -> None:
    cols = set(df.columns)
    missing = required - cols
    if missing:
        raise ValueError(f"{filename} está faltando colunas: {missing}")
