from fastapi import FastAPI, HTTPException
from typing import List, Dict
import os
import logging

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

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage for items
items: List[Dict] = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/favicon.ico")
def get_favicon():
    return {"message": "No favicon available"}

@app.get("/items")
def get_items():
    logger.info(f"Items endpoint accessed, items count: {len(items)}")
    return items

@app.post("/items")
def create_item(item: Dict):
    item_id = max([i["id"] for i in items], default=0) + 1
    item["id"] = item_id
    items.append(item)
    logger.info(f"Item created: {item}")
    return item

@app.put("/items/{id}")
def update_item(id: int, updated_item: Dict):
    for item in items:
        if item["id"] == id:
            item.update(updated_item)
            logger.info(f"Item updated: {item}")
            return item
    logger.warning(f"Item with id {id} not found for update")
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{id}")
def delete_item(id: int):
    for item in items:
        if item["id"] == id:
            items.remove(item)
            logger.info(f"Item deleted: {id}")
            return {"message": f"Item {id} deleted"}
    logger.warning(f"Item with id {id} not found for deletion")
    raise HTTPException(status_code=404, detail="Item not found")
