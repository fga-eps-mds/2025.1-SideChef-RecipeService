from pydantic import BaseModel
from typing import List, Optional

class Ingredient(BaseModel):
    name: str
    quantity: Optional[str] = ""

class Recipe(BaseModel):
    name: str
    type: str
    difficulty: str
    ingredients: List[Ingredient]
    prepare: str
    image_url: Optional[str] = None