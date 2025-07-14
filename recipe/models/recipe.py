from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    quantity: Optional[str] = ""
    ingredient: str



class Recipe(BaseModel):
    Name: str
    Type: str
    Difficulty: str
    Ingredients: List[Ingredient]
    Preparation: str
    image_url: Optional[str] = Field(None, description=" URL da imagem") 

