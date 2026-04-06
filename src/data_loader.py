import pandas as pd
import glob
import os

def load_dsa_data(folder_path):
    files = glob.glob(os.path.join(folder_path, "*.csv"))
    print(f"[DSA] Found {len(files)} files")

    df_list = []
    for file in files:
        try:
            df = pd.read_csv(file, low_memory=False)
            df_list.append(df)
        except Exception as e:
            print(f"Error: {file} -> {e}")

    combined = pd.concat(df_list, ignore_index=True)
    print(f"[DSA] Combined rows: {len(combined):,}")
    return combined


def load_jigsaw_data(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        print(f"[JIGSAW] Loaded {len(df):,} rows")
        return df
    else:
        print("[JIGSAW] File not found")
        return None