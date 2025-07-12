from pydantic import BaseModel
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
    image_url: Optional[str] = Field(None, description=" URL da imagem") 

