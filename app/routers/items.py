from fastapi import APIRouter, HTTPException
from app.models import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

# Fake in-memory database
fake_db = []

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    """Create a new item and store it in the fake database."""
    new_item = {**item.dict(), "id": len(fake_db) + 1}
    fake_db.append(new_item)
    return new_item

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Fetch an item by ID."""
    item = next((item for item in fake_db if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
