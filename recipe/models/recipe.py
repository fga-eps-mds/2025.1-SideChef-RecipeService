from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    quantidade: Optional[str] = ""
    ingrediente: str

class Recipe(BaseModel):
    Nome: str
    Tipo: str
    Dificuldade: str
    Ingredientes: List[Ingredient]
    Preparo: str