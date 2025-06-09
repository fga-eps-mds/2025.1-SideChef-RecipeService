from typing import Dict
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
    def make_recipe(id: str, name: str, recipe_type: str, difficulty: str, ingredients: list, preparation: str) -> Dict:
        recipe = {
            "_id": id,
            "Nome": name,
            "Tipo": recipe_type,
            "Dificuldade": difficulty,
            "Ingredientes": ingredients,
            "Preparo": preparation
        }
        return recipe
    
    input_recipe = {
        "Nome": "Bolo de Cenoura",
        "Tipo": "Doce",
        "Dificuldade": "Fácil",
        "Ingredientes": ["cenoura", "açúcar", "farinha"],
        "Preparo": "Bata tudo no liquidificador e leve ao forno por 30 minutos"
    }
        
    existing_recipe = make_recipe(
        id=str(random.randint(1, 1000)),
        name= "Milk Shake de Banana",
        recipe_type="Bebida Gelada",
        difficulty="Fácil",
        ingredients=["leite", "banana"],
        preparation="Bata tudo no liquidificador"

    )
    
@pytest.fixture
def mock_mongo_collection():
    collection = MagicMock()

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

    def mock_find_one(query: Dict = None, **kwargs) -> Dict:
        for doc in collection._mock_data:
            if query.get("Nome") == doc.get("Nome"):
                return doc.copy()
        return None
    
    def compile_pattern(pattern_input):
        ingredients_filter = pattern_input.get("Ingredientes", {})
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

    def mock_find(query: Dict = None, **kwargs):
        if not query:
            return collection._mock_data
        recipes = []
        query_all = query.get("$and")
        query_some = query.get("$or")
        if query_all:
            for data in collection._mock_data:
                ingredientes = data.get("Ingredientes", [])
                if all(any(compile_pattern(f).match(ing) for ing in ingredientes) for f in query_all):
                    recipes.append(data)
            return recipes
        # if query_some:
        #     for data in collection._mock_data:
        #         ingredientes = data.get("Ingredientes", [])
        #         if any(any(compile_pattern(f).match(ing) for ing in ingredientes) for f in query_all):
        #             recipes.append(data)
        #     return recipes

        ingredients_filter = query.get("Ingredientes", {})
        regex = ingredients_filter.get("$regex")
        options = ingredients_filter.get("$options", "")
        if regex:
            flags = re.IGNORECASE if "i" in options else 0
            pattern = re.compile(regex, flags)
            result = []
            for doc in collection._mock_data:
                if any(pattern.search(ing) for ing in doc.get("Ingredientes", [])):
                    result.append(doc)
            return result
        return []

    collection.find_one = MagicMock(side_effect=mock_find_one)

    collection.insert_one = MagicMock()

    collection.find = MagicMock(side_effect=mock_find)

    return collection

@pytest.fixture
def mock_mongo_db(mock_mongo_collection):
    db = MagicMock()
    db.__bool__.return_value = True
    db.__getitem__.return_value = mock_mongo_collection

    return db

@pytest.fixture
def test_client(mock_mongo_db, monkeypatch):
    monkeypatch.setattr('recipe.routes.recipe.db', mock_mongo_db)
    client = TestClient(app)

    yield client

@pytest.fixture
def test_client_no_db(monkeypatch):
    monkeypatch.setattr('recipe.routes.recipe.db', None)  
    client = TestClient(app)

    yield client

def test_create_recipe_success(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/createRecipes", json=MockData.input_recipe)
    input_recipe = MockData.input_recipe

    assert response.status_code == 200
    assert response.json() == {
        "message": "Recipe created successfully", 
        "recipe": input_recipe}
    # Testa se função mockada foi chamada uma vez com o devido parâmetro
    mock_mongo_collection.find_one.assert_called_once_with({"Nome": input_recipe["Nome"]})
    mock_mongo_collection.insert_one.assert_called_once_with(input_recipe)

def test_create_recipe_error_no_connection(test_client_no_db):
    
    response = test_client_no_db.post("/recipe/createRecipes", json=MockData.input_recipe)
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

    
def test_create_recipe_error_already_created(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/createRecipes", json=MockData.existing_recipe)

    assert response.status_code == 400
    assert response.json() == {"detail": "Recipe with this name already exists"}
    mock_mongo_collection.find_one.assert_called_once_with({"Nome": MockData.existing_recipe["Nome"]})
    mock_mongo_collection.insert_one.assert_not_called()
 

def test_filter_one_ingredient_success(test_client, mock_mongo_collection):
    response = test_client.get("/recipe/oneIngredient", params={"ingrediente": "leite"})

    assert response.status_code == 200
    response = response.json()
    recipes = response.get("recipes", [])

    assert len(recipes) == 2
    assert all("leite" in recipe["Ingredientes"] for recipe in recipes)

    mock_mongo_collection.find.assert_called_once_with({
        "Ingredientes": {"$regex": fr"\bleitea*o*s*\b", "$options": "i"}
    })

def test_filter_one_ingredient_no_connection(test_client_no_db):
    response = test_client_no_db.get("/recipe/oneIngredient", params={"ingrediente": "leite"})

    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

def test_filter_one_ingredient_empty_value(test_client):
    response = test_client.get("/recipe/oneIngredient", params={"ingrediente": ""})

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid ingredient format. Expected a non-empty string."
        }

def test_get_recipes_by_all_ingredients_success(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/allIngredients", json=["leite", "banana"])
    assert response.status_code == 200
    recipes = response.json().get("recipes")
    assert len(recipes) == 1
    assert recipes[0]["Nome"] == "Milk Shake de Banana"


def test_get_recipes_by_all_ingredients_no_connection(test_client_no_db):
    ...

def test_get_recipes_by_all_ingredients_empty_value(test_client):
    ...

def test_get_recipes_by_all_ingredients_invalid_value(test_client, mock_mongo_collection):
    ...