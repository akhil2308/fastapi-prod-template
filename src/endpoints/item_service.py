from fastapi import APIRouter, HTTPException, Depends, Body
from fastapi import Query

from sqlalchemy.orm import Session
from typing import Optional, Any

from src.crud import *
from src.schema import ItemCreate, Item as ItemSchema

from database import get_db

import logging
logger = logging.getLogger(__name__)

# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ItemSchema)
async def create_item_api(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@router.get("/{item_id}", response_model=ItemSchema)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/", response_model=list[ItemSchema])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db=db, skip=skip, limit=limit)

@router.put("/{item_id}", response_model=ItemSchema)
async def update_item_api(item_id: int, updated_item: ItemCreate, db: Session = Depends(get_db)):
    db_item = update_item(db=db, item_id=item_id, updated_item=updated_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=ItemSchema)
async def delete_item_api(item_id: int, db: Session = Depends(get_db)):
    db_item = delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
