from fastapi import FastAPI

app = FastAPI(
    title="OptiCrop API",
    version="1.0.0",
    description="Smart Agricultural Production Optimization Engine"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to OptiCrop API",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "server": "Healthy",
        "version": "1.0.0"
    }
