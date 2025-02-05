from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 1

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    created_at: datetime
    is_deleted: bool
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
