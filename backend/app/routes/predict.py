from fastapi import APIRouter

from app.schemas.prediction import CropPrediction

from app.ml.predict import predict_crop

router = APIRouter(

    prefix="/predict",

    tags=["Prediction"]

)


@router.post("/")
def recommendation(

    request: CropPrediction

):

    crop = predict_crop(

        request.nitrogen,

        request.phosphorus,

        request.potassium,

        request.temperature,

        request.humidity,

        request.ph,

        request.rainfall

    )

    return {

        "recommended_crop": crop

    }
