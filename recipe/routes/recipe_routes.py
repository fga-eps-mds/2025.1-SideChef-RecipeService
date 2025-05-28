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

#rotas

@router.post("/createRecipes/")
async def create_recipe(recipe: Recipe):
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    recipes_collection = db["recipes"]

    if recipes_collection.find_one({"Nome": recipe.Nome}):
        raise HTTPException(status_code=400, detail="Recipe with this name already exists")
    
    recipes_collection.insert_one(recipe.model_dump())
    return {"message": "Recipe created successfully", "recipe": recipe}
