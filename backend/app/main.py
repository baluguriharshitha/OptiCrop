from fastapi import FastAPI

app = FastAPI(
    title="OptiCrop API",
    version="1.0.0"
)


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
        "Server": "Healthy"
    }


@app.get("/about")
def about():

    return {
        "Application":
        "Smart Agricultural Production Optimization Engine"
    }
