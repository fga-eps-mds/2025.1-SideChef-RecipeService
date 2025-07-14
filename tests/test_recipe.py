from typing import Dict, List, Optional
import re
import random

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, AsyncMock

from main import app

# AsyncMock, MagicMock são objetos que simulam que simulam testes;
# Pode adicionar métodos, como objeto Mock, e atributos simulados;
# Side effect de Mocks executa uma função atribuída ao chamar o objeto;

class MockData:

    # Construtor do dicionário de receitas simuladas
    def make_recipe(id: str, name: str, recipe_type: str, difficulty: str, ingredients: list, preparation: str) -> Dict:
        recipe = {
            "_id": id,
            "Name": name,
            "Type": recipe_type,
            "Difficulty": difficulty,
            "Ingredients": ingredients,
            "Preparation": preparation
        }
        return recipe
    
    ingredient = {
        "ingredient": "açúcar",
        "quantity": "1 xícara"
    }

    ingredient2 = {
        "ingredient": "farinha",
        "quantity": "2 xícaras"
    }

    # Receita a inserir(sem id)
    input_recipe = {
        "Name": "Bolo de Cenoura",
        "Type": "Doce",
        "Difficulty": "Fácil",
        "Ingredients": [ingredient, ingredient2],
        "Preparation": "Bata tudo no liquidificador e leve ao forno por 30 minutos",
        "image_url": "https://example.com/bolo_cenoura.jpg"
    }
    
    # Receita a ser repetida
    existing_recipe = make_recipe(
        id=str(random.randint(1, 1000)),
        name= "Milk Shake de Banana",
        recipe_type="Bebida Gelada",
        difficulty="Fácil",
        ingredients=[ingredient, ingredient2],
        preparation="Bata tudo no liquidificador"

    )
    
# Simulação do banco de dados
@pytest.fixture
def mock_mongo_collection():
    # A coleção de receitas, onde posso performar operações
    collection = MagicMock()

    # Conjunto de dados simulados
    collection._mock_data = [
        MockData.make_recipe(
        id=str(random.randint(1, 1000)),
        name= "Milk Shake de Banana",
        recipe_type="Bebida Gelada",
        difficulty="Fácil",
        ingredients=["leite", "banana"],
        preparation="Bata tudo no liquidificador"

    ),
        MockData.make_recipe(
            id=str(random.randint(1, 1000)),
            name="Milk Shake de Morango",
            recipe_type="Bebida Gelada",
            difficulty="Fácil",
            ingredients=["leite", "morango"],
            preparation="Bata tudo no liquidificador"
        ), MockData.make_recipe(
            id=str(random.randint(1, 1000)),
            name="Bolo de Chocolate",
            recipe_type="Doce",
            difficulty="Fácil",
            ingredients=["chocolate", "açúcar", "farinha"],
            preparation="Bata tudo no liquidificador e leve ao forno por 30 minutos"
        ), 
    ]

    # Simulação de retorno de uma receita
    def mock_find_one(query: Dict = None, **kwargs) -> Dict:
        for doc in collection._mock_data:
            if query.get("Name") == doc.get("Name"):
                return doc.copy()
        return None
    
    # Recebe o dicionário onde se define o regex e retorna um padrão a ser testado
    def compile_pattern(pattern_input):
        ingredients_filter = pattern_input.get("Ingredients", {})
        if not ingredients_filter:
            raise ValueError("Filter")
        regex = ingredients_filter.get("$regex")
        options = ingredients_filter.get("$options", "")
        if not regex or not options:
            raise ValueError("Regex")
        flags = re.IGNORECASE if "i" in options else 0
        pattern = re.compile(regex, flags)
        if not pattern:
            raise ValueError("Pattern")
        return pattern

    # Retorna lista de documentos:
    ## query_all para allIngredients;
    ## query_name para Name opcional em getRecipes;
    ## Outro caso para oneIngredient;
    def mock_find(query: Dict = None, **kwargs):
        if not query:
            return collection._mock_data
        recipes = []
        query_all = query.get("$and")
        query_some = query.get("$or")
        query_name = query.get("Name")

        if query_all != None and isinstance(query_all, list):
            for data in collection._mock_data:
                Ingredients = data.get("Ingredients", [])
                if Ingredients is None:
                    Ingredients = []
                if all(any(compile_pattern(f).match(ing) for ing in Ingredients) for f in query_all):
                    recipes.append(data)
            return recipes
        if query_some != None and isinstance(query_some, list):
            for data in collection._mock_data:
                Ingredients = data.get("Ingredients", [])
                if Ingredients is None:
                    Ingredients = []
                if any(any(compile_pattern(f).match(ing) for ing in Ingredients) for f in query_some):
                    recipes.append(data)
            return recipes

        if query_name != None:
            for doc in collection._mock_data:
                if doc.get("Name") == query_name:
                    recipes.append(doc)
            return recipes

        ingredients_filter = query.get("Ingredients", {})
        regex = ingredients_filter.get("$regex")
        options = ingredients_filter.get("$options", "")
        if regex:
            flags = re.IGNORECASE if "i" in options else 0
            pattern = re.compile(regex, flags)
            result = []
            for doc in collection._mock_data:
                ings = doc.get("Ingredients", [])
                if ings is None:
                    ings = []
                if any(pattern.search(ing) for ing in ings):
                    result.append(doc)
            return result
        return []

    # Atribui as funções definidas à coleção, a fim de simulação;
    collection.find_one = MagicMock(side_effect=mock_find_one)
    collection.insert_one = MagicMock()
    collection.find = MagicMock(side_effect=mock_find)

    return collection

# Simula conexão com banco de dados;
# Retorna os dados do banco e é True; 
@pytest.fixture
def mock_mongo_db(mock_mongo_collection):
    db = MagicMock()
    db.__bool__.return_value = True
    db.__getitem__.return_value = mock_mongo_collection

    return db

# Aplica a conexão simulada do banco no código e instancia um client;
@pytest.fixture
def test_client(mock_mongo_db, monkeypatch):
    monkeypatch.setattr('recipe.routes.recipe_routes.db', mock_mongo_db)
    client = TestClient(app)

    yield client

# Caso e que não há conexão;
@pytest.fixture
def test_client_no_db(monkeypatch):
    monkeypatch.setattr('recipe.routes.recipe_routes.db', None)  
    client = TestClient(app)

    yield client

def test_create_recipe_success(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/createRecipes", json=MockData.input_recipe)
    input_recipe = MockData.input_recipe

    assert response.status_code == 200
    assert response.json() == {
        "message": "Recipe created successfully", 
        "recipe": input_recipe}

    mock_mongo_collection.find_one.assert_called_once_with({"Name": input_recipe["Name"]})
    mock_mongo_collection.insert_one.assert_called_once_with(input_recipe)

def test_create_recipe_error_no_connection(test_client_no_db):
    
    response = test_client_no_db.post("/recipe/createRecipes", json=MockData.input_recipe)
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

    
def test_create_recipe_error_already_created(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/createRecipes", json=MockData.existing_recipe)

    assert response.status_code == 400
    assert response.json() == {"detail": "Recipe with this name already exists"}
    mock_mongo_collection.find_one.assert_called_once_with({"Name": MockData.existing_recipe["Name"]})
    mock_mongo_collection.insert_one.assert_not_called()
 

def test_filter_one_ingredient_success(test_client, mock_mongo_collection):
    response = test_client.get("/recipe/oneIngredient", params={"ingredient": "leite"})

    assert response.status_code == 200
    response = response.json()
    recipes = response.get("recipes", [])

    assert len(recipes) == 2
    assert all("leite" in recipe["Ingredients"] for recipe in recipes)

    mock_mongo_collection.find.assert_called_once_with({
        "Ingredients": {"$regex": fr"\bleitea*o*s*\b", "$options": "i"}
    })

def test_filter_one_ingredient_no_connection(test_client_no_db):
    response = test_client_no_db.get("/recipe/oneIngredient", params={"ingredient": "leite"})

    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

def test_filter_one_ingredient_empty_value(test_client):
    response = test_client.get("/recipe/oneIngredient", params={"ingredient": ""})

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid ingredient format. Expected a non-empty string."
        }

def test_get_recipes_by_all_ingredients_success(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/allIngredients", json=["leite", "banana"])
    assert response.status_code == 200
    recipes = response.json().get("recipes")
    assert response.json().get("message") == "Found recipes with all ingredients"
    assert len(recipes) == 1
    assert recipes[0]["Name"] == "Milk Shake de Banana"

    expected_and_query = {
        "$and": [
            {"Ingredients": {"$regex": fr"\bleitea*o*s*\b", "$options": "i"}},
            {"Ingredients": {"$regex": fr"\bbananaa*o*s*\b", "$options": "i"}}
        ]
    }

    mock_mongo_collection.find.assert_called_once_with(expected_and_query)


def test_get_recipes_by_all_ingredients_no_connection(test_client_no_db, mock_mongo_collection):
    response = test_client_no_db.post("/recipe/allIngredients", json=["leite", "banana"])
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}
    mock_mongo_collection.find.assert_not_called()


def test_get_recipes_by_all_ingredients_empty_value(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/allIngredients", json=["", "   ", "\t"])
    assert response.status_code == 200
    assert response.json()["recipes"] == []
    assert response.json()["message"] == "There is no recipes with such ingredients"
    mock_mongo_collection.find.assert_not_called()

def test_get_recipes_by_all_ingredients_invalid_value(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/allIngredients", json=[1, 2, 3])
    assert response.status_code == 422
    mock_mongo_collection.find.assert_not_called()



def test_get_recipes_no_filter(test_client, mock_mongo_collection):
    response = test_client.get("/recipe/getRecipes")

    assert response.status_code == 200
    expected_data = [doc.copy() for doc in mock_mongo_collection._mock_data]
    assert response.json()["recipes"] == expected_data
    assert response.json()["message"] == "Found recipes with query"

    mock_mongo_collection.find.assert_called_once_with({})


def test_get_recipes_with_name_filter_found(test_client, mock_mongo_collection):
    name_to_filter = "Milk Shake de Banana"
    response = test_client.get(f"/recipe/getRecipes?name={name_to_filter}")

    assert response.status_code == 200

    expected_data = []
    for doc in mock_mongo_collection._mock_data:
        if doc["Name"] == name_to_filter:
            expected_data.append(doc)
    assert response.json()["recipes"] == expected_data
    assert response.json()["message"] == "Found recipes with query"
    assert len(response.json()["recipes"]) == 1
    mock_mongo_collection.find.assert_called_once_with({"Name": name_to_filter})


def test_get_recipes_with_name_filter_not_found(test_client, mock_mongo_collection):
    name_to_filter = "Torta de Maçã"
    response = test_client.get(f"/recipe/getRecipes?name={name_to_filter}")

    assert response.status_code == 200
    assert response.json()["recipes"] == []
    assert response.json()["message"] == "There is no recipes with query"

    mock_mongo_collection.find.assert_called_once_with({"Name": name_to_filter})

def test_get_recipes_empty_collection(test_client, mock_mongo_collection):
    original_data = mock_mongo_collection._mock_data.copy()
    mock_mongo_collection._mock_data.clear()

    response = test_client.get("/recipe/getRecipes")

    assert response.status_code == 200
    assert response.json()["recipes"] == []
    assert response.json()["message"] == "There is no recipes with query"

    mock_mongo_collection.find.assert_called_once_with({})

    mock_mongo_collection._mock_data.extend(original_data)

## testes someIngredients

def test_get_recipes_by_some_ingredients_success(test_client, mock_mongo_collection):
    
    response = test_client.post("/recipe/someIngredients", json=["leite", "chocolate"])

    assert response.status_code == 200
    response_data = response.json()
    recipes = response_data.get("recipes", [])

    assert response_data["message"] == "Found recipes with some ingredients"
    assert len(recipes) == 3 

    expected_or_query = {
        "$or": [
            {"Ingredients": {"$regex": fr"\bleitea*o*s*\b", "$options": "i"}},
            {"Ingredients": {"$regex": fr"\bchocolatea*o*s*\b", "$options": "i"}}
        ]
    }
    mock_mongo_collection.find.assert_called_once_with(expected_or_query)

def test_get_recipes_by_some_ingredients_not_found(test_client, mock_mongo_collection):
    
    response = test_client.post("/recipe/someIngredients", json=["jiló", "abacate"])

    assert response.status_code == 200
    response_data = response.json()
    recipes = response_data.get("recipes", [])

    assert response_data["message"] == "There is no recipe with such ingredients"
    assert recipes == []

    expected_or_query = {
        "$or": [
            {"Ingredients": {"$regex": fr"\bjilóa*o*s*\b", "$options": "i"}},
            {"Ingredients": {"$regex": fr"\babacatea*o*s*\b", "$options": "i"}}
        ]
    }
    mock_mongo_collection.find.assert_called_once_with(expected_or_query)


def test_get_recipes_by_some_ingredients_no_connection(test_client_no_db):

    response = test_client_no_db.post("/recipe/someIngredients", json=["leite"])

    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}


def test_get_recipes_by_some_ingredients_invalid_value(test_client):
  
    response = test_client.post("/recipe/someIngredients", json=[1, 2, 3])

    assert response.status_code == 422


def test_get_recipes_by_some_ingredients_empty_list(test_client, mock_mongo_collection):

    response = test_client.post("/recipe/someIngredients", json=[])

    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["message"] == "No valid ingredient as query"
    assert response_data["recipes"] == []

    mock_mongo_collection.find.assert_not_called()

def test_get_recipes_by_some_ingredients_empty_strings(test_client, mock_mongo_collection):

    response = test_client.post("/recipe/someIngredients", json=["", "   ", "\t"])

    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["message"] == "No valid ingredient as query"
    assert response_data["recipes"] == []

    mock_mongo_collection.find.assert_not_called()


## _success / _empty_list / _string with errors ;