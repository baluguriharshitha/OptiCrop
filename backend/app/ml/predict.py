import joblib

from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).parent / "crop_model.pkl"
model = joblib.load(MODEL_PATH)


def predict_crop(

    nitrogen,

    phosphorus,

    potassium,

    temperature,

    humidity,

    ph,

    rainfall

):

    prediction = model.predict([

        [

            nitrogen,

            phosphorus,

            potassium,

            temperature,

            humidity,

            ph,

            rainfall

        ]

    ])

    return prediction[0]
