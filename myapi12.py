from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
app=FastAPI()
class Items(BaseModel):
    item_name:str
    store_name:str
    price:float

item ={}
@app.post("/api/item/add/add-item/",response_model=Items)
async def add_item(item:Items):
    item.append(item.dict())
    return item