from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from recipe.models.recipe import Recipe
from core.database import db
from bson import ObjectId
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/recipe",
    tags=["Recipe"],
)

# endpoints

@router.post("/createRecipes/")
async def create_recipe(recipe: Recipe):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    recipes_collection = db["recipes"]

    if recipes_collection.find_one({"Nome": recipe.Nome}):
        raise HTTPException(status_code=400, detail="Recipe with this name already exists")
    
    recipes_collection.insert_one(recipe.model_dump())
    return {"message": "Recipe created successfully", "recipe": recipe}

@router.get("/getRecipes/")
# Might need to update CORS middleware and allow all origins to run on web verision of expo
async def get_recipes(name: Optional[str] = Query(None, description="Optional name filter for recipes")):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    recipes_collection = db["recipes"]

    query = {"name": name} if name else {}

    recipes = list(recipes_collection.find(query))

    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])
        if "Ingredientes" in recipe and isinstance(recipe["Ingredientes"], list):
            recipe["Ingredientes"] = [
                f"{ing.get('quantidade', '')} {ing.get('ingrediente', '')}".strip()
                for ing in recipe["Ingredientes"]
            ]

    return recipes