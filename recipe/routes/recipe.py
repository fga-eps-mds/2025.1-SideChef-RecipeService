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

@router.get("/items/")
async def list_items():
    items = await db["items"].find().to_list(100)
    return [
        {"id": str(item["_id"]), **{k: v for k, v in item.items() if k != "_id"}}
        for item in items
    ]

@router.get("/recipes")
def get_recipes():
    collection = db["recipes"]
    recipes = []
    for recipe in collection.find():
        recipe["id"] = str(recipe["_id"])
        recipe.pop("_id")
        recipe["Modo_de_Preparo"] = recipe.pop("Modo de Preparo", "")
        recipes.append(recipe)
    return recipes
