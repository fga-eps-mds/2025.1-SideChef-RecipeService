from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from recipe.models.recipe import Recipe
from core.database import db
from bson import ObjectId
from fastapi.responses import JSONResponse
from recipe.routes.route_functions import allIngredients , run_ocr

from fastapi import APIRouter, UploadFile, File
import recipe.routes.utils.ocr_utils as ocr

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





@router.post("/ocr_filter_recipies/")
async def ocr_filter_recipies(file: UploadFile = File(...)):
   
    file_contents = await file.read()
    extracted_text = run_ocr(file_contents)   
    extracted_text = extracted_text.lower()

    all_ingredients = ["leite"]
    ingredients = []
    for item in all_ingredients:
        if item in extracted_text:
          ingredients.append(item)

    recipies = allIngredients(ingredients)
    return recipies
