from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "DevOps Pipeline is working!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

