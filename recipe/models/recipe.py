from pydantic import BaseModel, Field
from typing import List

class Recipe(BaseModel):
    Nome: str
    Tipo: str
    Dificuldade: str
    Ingredientes: List[str]
    Preparo: str