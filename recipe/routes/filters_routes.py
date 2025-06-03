from typing import Optional
from fastapi import HTTPException, Query
from recipe.models.recipe import Recipe
from core.database import db
from bson import ObjectId
from fastapi.responses import JSONResponse

def one_ingredient(ingrediente : str):
                                #since it is a str and not a list, use regex     #accept plural
    print("search according to one item")                                               #case insensitive
    query = db["recipes"].find({"Ingredientes.ingrediente": {"$regex": fr"\b{ingrediente}a*o*s*\b", "$options": "i"}})        
    items = []
    for item in query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        items.append(item)
    return items

def all_ingredients(ingredients : list[str]):

    #make sure there are no white spaces
    ingredients_list = [item.strip() for item in ingredients]

    #create a list with the queries for each ingredient in the list
    filters = []
    for item in ingredients_list:
        f = {"Ingredientes.ingrediente": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
        filters.append(f)

    #search for recipes with all ingredients (operator "$and")
    query = db["recipes"].find({"$and": filters})
    items = []
    for item in query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        items.append(item)

    if not items:
        raise HTTPException(status_code=404, detail=f"There are no recipes with all these ingredients: {ingredients_list}")
    return {
        "recipes" : items
    }

    #if there are no recipes with all ingredients, search for one that has some of them (operator "$or")

def some_ingredients(ingredients : list[str]):

    #make sure that there are no white spaces
    ingredients_list = [item.strip() for item in ingredients]

    filters = []
    for item in ingredients_list:
        f = {"Ingredientes.ingrediente": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
        filters.append(f)


    or_query = db["recipes"].find({"$or": filters})
    some_items = []
    for item in or_query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        some_items.append(item)

    if some_items:
        return JSONResponse(content={
        "message": "There are no recipes with all the ingredients. Showing recipes with some of them.",
        "recipes": some_items
    })

    raise HTTPException(status_code=404, detail="There are no recipes with any of these ingredients.")