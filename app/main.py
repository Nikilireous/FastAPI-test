from fastapi import FastAPI, HTTPException, status

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
def search(q: str, page: int):
    if q in db:
        value = db[q]

        if 0 <= page - 1 <= len(q) - 1:
            return {"word": value[page - 1]}

        raise HTTPException(status.HTTP_404_NOT_FOUND, "page out of range")

    raise HTTPException(status.HTTP_404_NOT_FOUND, "key does not exist")
