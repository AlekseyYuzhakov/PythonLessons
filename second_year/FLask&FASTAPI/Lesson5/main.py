from fastapi import FastAPI
import logging
from Item import Item


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
async def root():
    logger.info("отработал GET запрос")
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):  # type: ignore
    logger.info("отработал GET запрос")
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f"отработал PUT запрос для item id = {item_id}")
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"отработал Delete запрос для item id = {item_id}")
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    logger.info("отработал POST запрос")
    return item


# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "description": "New description of the of object", "price": 9.99, "tax": 0.99}'