from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DSA_PATH = ROOT_DIR / "data" / "dsa"
JIGSAW_PATH = ROOT_DIR / "data" / "jigsaw.csv"
OUTPUT_PATH = ROOT_DIR / "outputs"
SAMPLE_SIZE = 100_000

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
