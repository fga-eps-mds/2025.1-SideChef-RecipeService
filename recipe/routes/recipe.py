from fastapi import APIRouter, HTTPException
from recipe.models.recipe import Item
from core.database import db
from bson import ObjectId

router = APIRouter(
    prefix="/recipe",
    tags=["Recipe"],
)

@router.post("/items/")
async def create_item(item: Item):
    result = await db["items"].insert_one(item.dict())
    return {"id": str(result.inserted_id)}

# @router.get("/items/")
# async def list_items():
#     items = await db["items"].find().to_list(100)
#     return [
#         {"id": str(item["_id"]), **{k: v for k, v in item.items() if k != "_id"}}
#         for item in items
#     ]

@router.get("/oneIngredient")
def get_recipes(ingrediente : str):
                                #como é uma str e não uma list usa regex     #aceitar plural
    print("procura de acordo com um item")                                               #case insensitive
    query = db["recipes"].find({"Ingredientes": {"$regex": fr"\b{ingrediente}a*o*s*\b", "$options": "i"}})        
    items = []
    for item in query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        items.append(item)
    return items


#usar o método post, porque get não suportou entrada de dados mais complexos como listas
@router.post("/allIngredients")
def get_recipes(ingredients : list[str]):

    ingredientsList = []
    #garantir que não tem nenhum espaço em branco
    for item in ingredients:
        ingredientsList.append(item.strip())

    #criar um lsita com as querys de cada ingrediente da lista
    filters = []
    for item in ingredientsList:
        f = {"Ingredientes": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
        filters.append(f)

    #buscar receitas com todos os ingredientes (operador "$and")
    query = db["recipes"].find({
        "$and": filters
    })

    items = []
    for item in query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        items.append(item)

    if not items:
        raise HTTPException(status_code=404, detail="Não há receitas com todos esses ingredientes.")
    return items

