def find_column(df, keywords):
    for kw in keywords:
        for col in df.columns:
            if kw.lower() in col.lower():
                return col
    return None