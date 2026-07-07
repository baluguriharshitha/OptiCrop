import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]

DATASET_PATH = BASE_DIR / "dataset" / "Crop_recommendation.csv"


def load_dataset():

    return pd.read_csv(DATASET_PATH)
