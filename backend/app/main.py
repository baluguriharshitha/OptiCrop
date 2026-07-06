from fastapi import FastAPI

from app.routes.auth import router as auth_router

app = FastAPI(
    title="OptiCrop API",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():

    return {
        "Project": "OptiCrop",
        "Status": "Running"
    }


@app.get("/health")
def health():

    return {
        "Server": "Healthy"
    }
