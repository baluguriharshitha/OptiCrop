from pathlib import Path

import joblib


MODEL_PATH = Path(__file__).parent / "crop_model.pkl"


def load_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(

            "Model not trained."

        )

    return joblib.load(MODEL_PATH)
