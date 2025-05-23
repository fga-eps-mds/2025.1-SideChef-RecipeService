from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2
import pytesseract
import recipe.routes.utils.ocr_utils as ocr
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
    try:
        # Read file
      file_contents = await file.read()

        # Convert to NumPy array then cv2 format
      np_array = np.frombuffer(file_contents, np.uint8)
      image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
      
      if image is None:
        return {"error": "Image not found"}

      process_image = ocr.Enhance(image)  # Initialize class with target image
      processed_image = process_image.execute()  # Run execute function

        # Extract and return OCR result
      extracted_text = pytesseract.image_to_string(processed_image,
                                                    lang='por',
                                                    config='--oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                                                  )
      
      # cut_text = extracted_text.split('\n')[0]  # Fetch only first line
      # print(cut_text.strip())  # For development only
      # process_image.show_steps()  # Show desired steps from image enhancing process (development only)

      all_ingredients = ["leite"]
      ingredients = []
      extracted_text = extracted_text.lower()
      for item in all_ingredients:
        if item in extracted_text:
          ingredients.append(item)

  #garantir que não tem nenhum espaço em branco
      ingredientsList = [item.strip() for item in ingredients]

      #criar um lista com as querys de cada ingrediente da lista
      filters = []
      for item in ingredientsList:
          f = {"Ingredientes": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
          filters.append(f)

      #buscar receitas com todos os ingredientes (operador "$and")
      query = db["recipes"].find({"$and": filters})
      items = []
      for item in query:
          item["id"] = str(item["_id"])
          item.pop("_id")
          items.append(item)

      if not items:
          raise HTTPException(status_code=404, detail="Não há receitas com todos esses ingredientes.")
      return {
          "recipies" : items
      }

    except Exception as err:
      return {"error": f"File upload failed: {str(err)}"}
    


"""
use as base to integrate as create new routes 
"""


# @router.get("/getRecipes")
# async def get_recipes(name: Optional[str] = Query(None, description="Optional name filter for recipes")):
#     if db is None:
#         raise HTTPException(status_code=500, detail="Database connection error")

#     recipes_collection = db["recipes"]

#     query = {"name": name} if name else {}

#     recipes = list(recipes_collection.find(query))

#     for recipe in recipes:
#         recipe["_id"] = str(recipe["_id"])

#     return recipes

# @router.get("/oneIngredient")
# def get_recipes(ingrediente : str):
#                                 #como é uma str e não uma list usa regex     #aceitar plural
#     print("procura de acordo com um item")                                               #case insensitive
#     query = db["recipes"].find({"Ingredientes": {"$regex": fr"\b{ingrediente}a*o*s*\b", "$options": "i"}})        
#     items = []
#     for item in query:
#         item["id"] = str(item["_id"])
#         item.pop("_id")
#         items.append(item)
#     return items


# #usar o método post, porque get não suportou entrada de dados mais complexos como listas
# @router.post("/allIngredientss")
# def get_recipes(ingredients : list[str]):

#     #garantir que não tem nenhum espaço em branco
#     ingredientsList = [item.strip() for item in ingredients]

#     #criar um lista com as querys de cada ingrediente da lista
#     filters = []
#     for item in ingredientsList:
#         f = {"Ingredientes": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
#         filters.append(f)

#     #buscar receitas com todos os ingredientes (operador "$and")
#     query = db["recipes"].find({"$and": filters})
#     items = []
#     for item in query:
#         item["id"] = str(item["_id"])
#         item.pop("_id")
#         items.append(item)

#     if not items:
#         raise HTTPException(status_code=404, detail="Não há receitas com todos esses ingredientes.")
#     return {
#         "recipies" : items
#     }

#     #se não tiver receitas com todos os ingredientes, buscar uma que tenha alguns deles (operador "$or")
# @router.post("/SomeIngredientss")
# def get_recipes(ingredients : list[str]):

#     #garantir que não tem nenhum espaço em branco
#     ingredientsList = [item.strip() for item in ingredients]

#     filters = []
#     for item in ingredientsList:
#         f = {"Ingredientes": {"$regex": fr"\b{item}a*o*s*\b", "$options": "i"}}
#         filters.append(f)


#     or_query = db["recipes"].find({"$or": filters})
#     some_items = []
#     for item in or_query:
#         item["id"] = str(item["_id"])
#         item.pop("_id")
#         some_items.append(item)

#     if some_items:
#         return JSONResponse(content={
#         "message": "Não há receitas com todos os ingredientes. Mostrando receitas com alguns deles.",
#         "recipies": some_items
#     })

#     raise HTTPException(status_code=404, detail="Não há receitas com nenhum desses ingredientes.")
