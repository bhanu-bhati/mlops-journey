from fastapi import FastAPI

# Initialize the API engine
app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "My first MLOps API is live on my M1 Mac!",
        "developer": "Bhanu Bhati",
    }

