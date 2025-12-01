import pandas as pd
from .config import Config

def score_match(user_skills: list, job_skills: list) -> tuple:
    overlap = set(user_skills) & set(job_skills)
    return len(overlap) * Config.SCORE_PER_SKILL, sorted(list(overlap))

def build_message(user_name: str, job: pd.Series, score: int, matched_skills: list) -> str:
    skills_str = ", ".join(matched_skills) if matched_skills else "—"
    return (
        f"{user_name}, esta vaga pode ser ideal para você: {job['title']} em {job['company']} "
        f"({job['location']}, nível {job['level']}). Compatibilidade {score} "
        f"pelas habilidades: {skills_str}."
    )

def recommend_jobs_for_user(user_row: pd.Series, jobs_df: pd.DataFrame) -> list:
    user_skills = user_row["skills_norm"]
    scored = []
    for _, job in jobs_df.iterrows():
        score, matched = score_match(user_skills, job["required_skills_norm"])
        if score >= Config.MIN_SCORE:
            scored.append({"job": job, "score": score, "matched_skills": matched})
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:Config.MAX_RECS_PER_USER]
