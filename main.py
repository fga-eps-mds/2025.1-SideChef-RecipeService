from fastapi import FastAPI, HTTPException, Query
from recipe.routes.recipe import router
from models import Recipe
from db import get_db
from typing import List, Optional

app = FastAPI()

app.include_router(router)


@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "running"}


@app.post("/recipes/")
async def create_recipe(recipe: Recipe):
    db = get_db()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    recipes_collection = db["recipes"]

    if recipes_collection.find_one({"name": recipe.name}):
        raise HTTPException(status_code=400, detail="Recipe with this name already exists")
    
    recipes_collection.insert_one(recipe.model_dump())
    return {"message": "Recipe created successfully", "recipe": recipe}


@app.get("/recipes", tags=["Recipes"])
async def get_recipes(name: Optional[str] = Query(None, description="Optional name filter for recipes")):
    db = get_db()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    recipes_collection = db["recipes"]

    query = {"name": name} if name else {}

    recipes = list(recipes_collection.find(query))

    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])

    return recipes