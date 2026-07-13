from fastapi import FastAPI

app = FastAPI()

@app.put("/student/{id}")
def update(id: int):
    return {"id": id}