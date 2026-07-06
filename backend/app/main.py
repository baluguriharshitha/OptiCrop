from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.predict import router as predict_router
app.include_router(auth_router)
app.include_router(predict_router)

app = FastAPI(
    title="OptiCrop API",
    version="1.0.0",
    description="Smart Agricultural Production Optimization Engine"
)

app.include_router(auth_router)


@app.get("/")
def home():

    return {
        "Project": "OptiCrop",
        "Status": "Running",
        "Version": "1.0.0"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }
