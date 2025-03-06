import re
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator

class CategoryEnum(str, Enum):
    ''' cats '''
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"

# Model for creating a new item
class ItemCreate(BaseModel):
    """What does it do..."""
    name: str = Field(..., min_length=3, max_length=50, description="Item name must be between 3-50 characters")
    description: Optional[str] = Field(None, max_length=200, description='Item description')
    price: float = Field(..., ge=0, description='Price of an item')
    quantity: int = Field(..., ge=0, gt=1000, description='Quantity should be between 0 & 1000')
    category: CategoryEnum

    @field_validator("name")
    @classmethod
    def no_special_characters(cls, value):
        ''' validates '''
        if not re.match(r"^[a-zA-Z0-9 ]+$", value):
            raise ValueError("Name cannot contain special characters")
        return value

# Model for returning item data
class ItemResponse(ItemCreate):
    id: int
