import pandas as pd
from scipy import stats

def platform_distribution(df, platform_col):
    return df[platform_col].value_counts()


def automation_rate(df, platform_col, auto_col):
    result = (
        df.groupby(platform_col)[auto_col]
        .apply(lambda x: (x.astype(str).str.lower().isin(["true","1","yes"])).mean() * 100)
    )
    return result.sort_values(ascending=False)


def toxicity_stats(df):
    return df["toxicity_score"].describe()


def correlation_analysis(df1, df2, col1, col2):
    r, p = stats.pearsonr(df1[col1], df2[col2])
    return r, p