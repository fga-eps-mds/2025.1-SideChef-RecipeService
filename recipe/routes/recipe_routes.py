from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from recipe.models.recipe import Recipe
from core.database import db
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/recipe",
    tags=["Recipe"],
)

@router.post("/createRecipes/")
async def create_recipe(recipe: Recipe):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    recipes_collection = db["recipes"]

    if recipes_collection.find_one({"name": recipe.name}):
        raise HTTPException(status_code=400, detail="Recipe with this name already exists")
    
    recipes_collection.insert_one(recipe.model_dump())
    return {"message": "Recipe created successfully", "recipe": recipe}


@router.get("/getRecipes/")
async def get_recipes(name: Optional[str] = Query(None, description="Optional name filter for recipes")):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    recipes_collection = db["recipes"]

    query = {"name": name} if name else {}

    recipes = list(recipes_collection.find(query))

    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])
        # Aqui você pode manter a estrutura original, ou formatar melhor os ingredientes:
        # Por exemplo: "2 cups sugar"
        if "ingredients" in recipe and isinstance(recipe["ingredients"], list):
            recipe["ingredients"] = [
                f"{ing.get('quantity', '')} {ing.get('name', '')}".strip()
                for ing in recipe["ingredients"]
            ]

    return recipes
