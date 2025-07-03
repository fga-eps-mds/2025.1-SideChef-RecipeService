from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    quantidade: Optional[str] = ""
    ingrediente: str

#Need to change the var's name to english here ASasASasand in "SideChef-Mobile"!

#Need to change the var's name to english here and in "SideChef-Mobile"!
class Recipe(BaseModel):
    Nome: str
    Tipo: str
    Dificuldade: str
    Ingredientes: List[Ingredient]
    Preparo: str
    image_url: Optional[str] = Field(None, description=" URL da imagem") 

class Test():
    Nome: str