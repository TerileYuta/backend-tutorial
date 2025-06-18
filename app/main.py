from fastapi import FastAPI

app = FastAPI(title="tutorial")

@app.get("/")
async def home():
    return {"message": "Hello, World"}