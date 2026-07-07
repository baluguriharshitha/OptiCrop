from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.predict import router as predict_router

app = FastAPI(
    title="OptiCrop API",
    description="Smart Agricultural Production Optimization Engine",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development/demo. Later you can replace "*" with your frontend URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(predict_router)

@app.get("/")
def home():
    return {
        "application": "OptiCrop",
        "status": "Running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
