import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_platform_distribution(series, output_path):
    plt.figure(figsize=(10,5))
    series.head(10).plot(kind="barh")
    plt.title("Top Platforms by Moderation Volume")
    plt.xlabel("Count")
    plt.tight_layout()
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, "platform_distribution.png"))
    plt.close()


def plot_heatmap(df, output_path):
    plt.figure(figsize=(12,5))
    sns.heatmap(df, cmap="YlOrRd", annot=True)
    plt.title("Decision Grounds Heatmap")
    plt.tight_layout()
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, "heatmap.png"))
    plt.close()


def plot_toxicity(df, output_path):
    plt.figure(figsize=(8,5))
    df["toxicity_score"].value_counts().sort_index().plot(kind="bar")
    plt.title("Toxicity Distribution")
    plt.tight_layout()
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, "toxicity.png"))
    plt.close()