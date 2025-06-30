from fastapi import FastAPI, HTTPException
from typing import List, Dict
from langsmith import Client
import os

app = FastAPI(
    title="FastAPI Sample REST API",
    description="A simple FastAPI application exposing REST endpoints for managing items. AI agents can interact with this API to retrieve, create, update, and delete items.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "url": "https://example.com/contact",
        "email": "support@example.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Initialize LangSmith client with error handling
api_key = os.getenv("LANGSMITH_API_KEY")
if not api_key:
    raise RuntimeError("LangSmith API key is missing. Please set the LANGSMITH_API_KEY environment variable.")
langsmith_client = Client(api_key=api_key)

# In-memory storage for items
items: List[Dict] = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

@app.get("/")
def read_root():
    langsmith_client.log("GET /", {"message": "Root endpoint accessed"})
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/favicon.ico")
def get_favicon():
    return {"message": "No favicon available"}

@app.get("/items")
def get_items():
    langsmith_client.log("GET /items", {"items_count": len(items)})
    return items

@app.post("/items")
def create_item(item: Dict):
    item_id = max([i["id"] for i in items], default=0) + 1
    item["id"] = item_id
    items.append(item)
    langsmith_client.log("POST /items", {"item_created": item})
    return item

@app.put("/items/{id}")
def update_item(id: int, updated_item: Dict):
    for item in items:
        if item["id"] == id:
            item.update(updated_item)
            langsmith_client.log("PUT /items/{id}", {"item_updated": item})
            return item
    langsmith_client.log("PUT /items/{id}", {"error": "Item not found"})
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{id}")
def delete_item(id: int):
    for item in items:
        if item["id"] == id:
            items.remove(item)
            langsmith_client.log("DELETE /items/{id}", {"item_deleted": id})
            return {"message": f"Item {id} deleted"}
    langsmith_client.log("DELETE /items/{id}", {"error": "Item not found"})
    raise HTTPException(status_code=404, detail="Item not found")
