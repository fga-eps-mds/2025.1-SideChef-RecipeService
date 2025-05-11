from pydantic import BaseModel
from typing import List 


class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    preparation: str
    preparation_time: str #exemplo "30 minutos" 
    portions: int