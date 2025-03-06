'''It hold information'''
from fastapi import APIRouter, HTTPException, Path, Query
from app.models import ItemCreate, ItemResponse

# Fake in-memory database
fake_db = []

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    """Create a new item and store it in the fake database."""
    new_item = {**item.dict(), "id": len(fake_db) + 1}
    fake_db.append(new_item)
    print('post/items/')
    return new_item

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int = Path(..., gt=0, description="Item ID must be positive")):
    """Fetch an item by ID."""
    item = next((item for item in fake_db if item["id"] == item_id), None)
    print('get/items/id')
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/searchh/")
async def search_item(name: str = Query(..., min_length=3, description="Search tearm must be at least 3 character long")):
    """Search item by name"""
    res = [item for item in fake_db if (name.lower() == item["name"].lower())]
    return res or {"message": "No Item Found"}