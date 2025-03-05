from pydantic import BaseModel
from typing import Optional

# Model for creating a new item
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

# Model for returning item data
class ItemResponse(ItemCreate):
    id: int
