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

@router.post("/createRecipes")
def create_recipe(recipe: Recipe):
    
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    recipes_collection = db["recipes"]

    duplicate_recipe = recipes_collection.find_one({"Nome": recipe.Nome})

    if duplicate_recipe:
        raise HTTPException(status_code=400, detail="Recipe with this name already exists")
    
    recipes_collection.insert_one(recipe.model_dump())
    return {"message": "Recipe created successfully", "recipe": recipe}


@router.get("/getRecipes")
def get_recipes(name: Optional[str] = Query(None, description="Optional name filter for recipes")):
    # JP:
    ## Implementar:
    ### (!) Validação extra para garantir que name é uma string não vazia ou tipo incompatível;
    ## Testar:
    ### (!) Retorno de lista de receitas;
    ### (!) db == None;
    ### (!) name == None ou name == ""; 
    
    # Simular db
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    recipes_collection = db["recipes"]

    query = {"Nome": name} if name else {}

    recipes = list(recipes_collection.find(query))

    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])

    message = "Found recipes with query"

    if len(recipes) == 0:
        message = "There is no recipes with query"
    return {
        "recipes" : recipes,
        "message" : message 
    }


@router.get("/oneIngredient")
def get_recipes_by_one(ingrediente: str):

    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    if not isinstance(ingrediente, str) or not ingrediente.strip():
        raise HTTPException(status_code=400, detail="Invalid ingredient format. Expected a non-empty string.")

    # como é uma str e não uma list usa regex   
    # aceitar plural
    print("procura de acordo com um item")                                               
    # case insensitive
    query = db["recipes"].find({"Ingredientes": {"$regex": fr"\b{ingrediente}a*o*s*\b", "$options": "i"}})        
    items = []
    for item in query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        items.append(item)
    
    message = "Found recipes with ingredient"

    if len(items) == 0:
        message = "There is no recipes with ingredient"
    return {
        "recipes" : items,
        "message" : message 
    }


#usar o método post, porque get não suportou entrada de dados mais complexos como listas
@router.post("/allIngredients")
def get_recipes_by_all(ingredients : list[str]):
    # Vinícius:
    ## Implementar:
    ## Testar:
    ### (!) Retorno de lista de receitas filtradas por todos os ingredientes;
    ### (!) db == None;
    ### (!) ingredientes inválidos (ex: número, string vazia, etc).

    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    #garantir que não tem nenhum espaço em branco
    ingredientsList = [item.strip() for item in ingredients]
    if not ingredientsList:
        return {
            "recipes" : [],
            "message" : "There is no recipes with such ingredients"
        }

    #criar um lista com as querys de cada ingrediente da lista
    filters = []
    for item in ingredientsList:
        if item in ["", "   ", "\t"]:
            return {
                "recipes" : [],
                "message" : "There is no recipes with such ingredients"
            }
        f = {"Ingredientes": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
        filters.append(f)

    #buscar receitas com todos os ingredientes (operador "$and")
    query = db["recipes"].find({"$and": filters})
    items = []
    for item in query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        items.append(item)

    message = "Found recipes with all ingredients"

    if len(items) == 0:
        message = "There is no recipes with such ingredients"
    return {
        "recipes" : items,
        "message" : message 
    }

    #se não tiver receitas com todos os ingredientes, buscar uma que tenha alguns deles (operador "$or")
@router.post("/someIngredients")
def get_recipes_by_some(ingredients : list[str]):

    if db is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    ingredientsList = [item.strip() for item in ingredients if item and item.strip()]

    if not ingredientsList:
        return JSONResponse(
            status_code=200,
            content={
                "message": "No valid ingredient as query",
                "recipes": []
            }
        )
    
    recipes_collection = db["recipes"]
    filters = []
    for item in ingredientsList:
        f = {"Ingredientes": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
        filters.append(f)

    or_query = recipes_collection.find({"$or": filters})

    some_items = []
    for item in or_query:
        item["id"] = str(item["_id"])
        item.pop("_id")
        some_items.append(item)

    if not some_items:
        message = "There is no recipe with such ingredients"
    else:
        message = "Found recipes with some ingredients"

    return JSONResponse(
        status_code=200,
        content={
            "message": message,
            "recipes": some_items
        }
    )
