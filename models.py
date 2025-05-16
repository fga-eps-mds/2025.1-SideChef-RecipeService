from pydantic import BaseModel
from typing import List 


class Recipe(BaseModel):
    name: str
    type: str
    difficulty: int
    ingredients: List[str]
    preparation: str