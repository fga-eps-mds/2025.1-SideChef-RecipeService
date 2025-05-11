from fastapi import FastAPI, HTTPException
from recipe.routes.recipe import router
from models import Recipe
from db import get_db

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