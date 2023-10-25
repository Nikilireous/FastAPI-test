from fastapi import FastAPI

app = FastAPI()

db = {
    "a": ["one", "two", "three"],
    "b": ["four", "five", "six"],
    "c": ["seven", "eight", "nine"]
}


@app.get("/")
def index():
    return {"works": True}


@app.post("/users")
def registration():
    return {"name": "Nikita"}


@app.get("/search")
def search(q: str):
    print(q)
    return "OK"
