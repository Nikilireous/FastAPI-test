from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"works": True}


@app.post("/users")
def registration():
    return {"name":"Nikita"}

@app.get("/search")
def search(q: str):
    print(q)
    return "OK"
