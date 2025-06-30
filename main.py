from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"}
    ]
