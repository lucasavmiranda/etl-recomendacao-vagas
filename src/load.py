import pandas as pd
from datetime import datetime
from .config import Config
from .utils import log

def next_news_id(existing_df: pd.DataFrame) -> int:
    if existing_df.empty:
        return 1
    return int(existing_df["news_id"].max()) + 1

def news_exists(existing_df: pd.DataFrame, user_id: int, description: str) -> bool:
    subset = existing_df[(existing_df["user_id"] == user_id) & (existing_df["description"] == description)]
    return not subset.empty

def append_news(existing_df: pd.DataFrame, user_id: int, description: str, icon_url: str = Config.ICON_URL) -> pd.DataFrame:
    if news_exists(existing_df, user_id, description):
        log(f"News já existe (user_id={user_id}). Pulando.")
        return existing_df
    nid = next_news_id(existing_df)
    new_row = {
        "user_id": user_id,
        "news_id": nid,
        "icon": icon_url,
        "description": description,
        "created_at": datetime.now().isoformat(timespec="seconds")
    }
    return pd.concat([existing_df, pd.DataFrame([new_row])], ignore_index=True)

def save_news(df: pd.DataFrame, path: str = Config.USER_NEWS_CSV) -> None:
    df.to_csv(path, index=False)
    log(f"Salvo em {path}")
