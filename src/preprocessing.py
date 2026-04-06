def sample_data(df, n=300000):
    if len(df) > n:
        df = df.sample(n=n, random_state=42)
        print(f"[Sampling] Reduced to {n}")
    return df


def filter_child_safety(df, category_col):
    keywords = ["child", "minor", "csam", "grooming", "sexual"]
    return df[df[category_col].str.lower().str.contains("|".join(keywords), na=False)]


def create_toxicity_score(df):
    toxic_cols = ["toxic","severe_toxic","obscene","threat","insult","identity_hate"]
    df["toxicity_score"] = df[toxic_cols].sum(axis=1)
    return df