from typing import Dict
from collections import OrderedDict

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, AsyncMock

from main import app
from recipe.models.recipe import Recipe

# AsyncMock, MagicMock são objetos que simulam que simulam testes;
# Pode adicionar métodos, como objeto Mock, e atributos simulados;
# Side effect de Mocks executa uma função atribuída ao chamar o objeto;

class MockData:
    def make_recipe(name: str, recipe_type: str, difficulty: str, ingredients: list, preparation: str) -> OrderedDict:
        return Recipe(
            Nome=name,
            Tipo=recipe_type,
            Dificuldade=difficulty,
            Ingredientes=ingredients,
            Preparo=preparation
        ).model_dump()
    
    single_recipe = Recipe(
        Nome="Bolo de Cenoura",
        Tipo="Doce",                    
        Dificuldade="Fácil",
        Ingredientes=["cenoura", "açúcar", "farinha"],
        Preparo="Bata tudo no liquidificador e leve ao forno por 30 minutos"
    ).model_dump()
        
    existing_recipe = Recipe(
        Nome="Milk Shake de Banana",
        Tipo="Bebida Gelada",
        Dificuldade="Fácil",
        Ingredientes=["leite", "banana"],
        Preparo="Bata tudo no liquidificador").model_dump()
    
@pytest.fixture
def mock_mongo_collection():
    collection = AsyncMock()

    collection._mock_data = [
        MockData.existing_recipe,
        MockData.make_recipe(
            name="Milk Shake de Morango",
            recipe_type="Bebida Gelada",
            difficulty="Fácil",
            ingredients=["leite", "morango"],
            preparation="Bata tudo no liquidificador"
        )
    ]

    async def mock_find_one(query: Dict = None, **kwargs) -> Dict:
        for doc in collection._mock_data:
            if query.get("Nome") == doc.get("Nome"):
                return doc.copy()
        return None

    # Testar se funciona
    collection.find_one = AsyncMock(side_effect=mock_find_one)
    # Testar se funciona
    collection.insert_one = AsyncMock()

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
    response = test_client.post("/recipe/createRecipes", json=MockData.single_recipe)
    single_recipe = MockData.single_recipe

    assert response.status_code == 200
    assert response.json() == {
        "message": "Recipe created successfully", 
        "recipe": single_recipe}
    # Testa se função mockada foi chamada uma vez com o devido parâmetro
    mock_mongo_collection.find_one.assert_awaited_once_with({"Nome": single_recipe["Nome"]})
    mock_mongo_collection.insert_one.assert_awaited_once_with(single_recipe)

def test_create_recipe_error_no_connection(test_client_no_db):
    
    response = test_client_no_db.post("/recipe/createRecipes", json=MockData.single_recipe)
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

    
def test_create_recipe_error_already_created(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/createRecipes", json=MockData.existing_recipe)
    existing_recipe = MockData.existing_recipe

    assert response.status_code == 400
    assert response.json() == {"detail": "Recipe with this name already exists"}
    mock_mongo_collection.find_one.assert_awaited_once_with({"Nome": existing_recipe["Nome"]})
    mock_mongo_collection.insert_one.assert_not_awaited()
 