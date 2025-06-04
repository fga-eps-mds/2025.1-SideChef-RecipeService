from typing import Dict, List, Optional

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, AsyncMock, patch

from main import app

single_recipe = {
        "Nome": "Bolo de Caneca",
        "Tipo": "Doce",
        "Dificuldade": "Fácil",
        "Ingredientes":  ["Massa", "ovo", "2 colheres (sopa) de achocolatado em pó", "3 colheres (sopa) rasas de açúcar", "4 colheres (sopa) rasas de farinha de trigo", "1 colher (sopa) de óleo", "fermento em pó químico", "1 colher (café) rasa de fermento em pó"],
        "Preparo": "Bata até atingir forma adequada"
    }


@pytest.fixture
def mock_mongo_collection():
    collection = AsyncMock()

    collection._mock_data = [
        {"_id": "1", "Nome": "Milk Shake de Banana", "Tipo": "Bebida Gelada", "Dificuldade" : "Fácil", "Ingredientes": ["leite", "banana"], "Preparo": "Bata tudo no liquidificador"},
        {"_id": "2", "Nome": "Milk Shake de Morango", "Tipo": "Bebida Gelada", "Dificuldade" : "Fácil", "Ingredientes": ["leite", "morando"], "Preparo": "Bata tudo no liquidificador"},
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


def test_create_recipe(test_client, mock_mongo_collection):
    response = test_client.post("/recipe/createRecipes", json=single_recipe)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Recipe created successfully", 
        "recipe": single_recipe}
    mock_mongo_collection.find_one.assert_awaited_once_with({"Nome": single_recipe["Nome"]})
    mock_mongo_collection.insert_one.assert_awaited_once_with(single_recipe)

# teste getRecipe

@pytest.fixture
def mock_mongo_collection():
    collection = AsyncMock()

    collection._mock_data = [
        {"_id": "1", "Nome": "Milk Shake de Banana", "Tipo": "Bebida Gelada", "Dificuldade" : "Fácil", "Ingredientes": ["leite", "banana"], "Preparo": "Bata tudo no liquidificador"},
        {"_id": "2", "Nome": "Milk Shake de Morango", "Tipo": "Bebida Gelada", "Dificuldade" : "Fácil", "Ingredientes": ["leite", "morango"], "Preparo": "Bata tudo no liquidificador"}
    ]

    async def mock_find_one(query: Dict = None, **kwargs) -> Optional[Dict]:
        for doc in collection._mock_data:
            if query and query.get("Nome") == doc.get("Nome"):
                return doc.copy()
        return None

    def mock_find_synchronous(query: Dict = None, **kwargs) -> List[Dict]:
        results = []
        data_to_search = [doc.copy() for doc in collection._mock_data]

        if not query:
            results = data_to_search
        else:
            name_filter = query.get("Nome")
            if name_filter is not None:
                for doc in data_to_search:
                    if doc.get("Nome") == name_filter:
                        results.append(doc)
        return results

    collection.find_one = AsyncMock(side_effect=mock_find_one)
    collection.find = MagicMock(side_effect=mock_find_synchronous)
    collection.insert_one = AsyncMock()
    collection.update_one = AsyncMock()
    collection.delete_one = AsyncMock()

    return collection

def test_get_all_recipes_no_filter(test_client, mock_mongo_collection):
    response = test_client.get("/recipe/getRecipes")

    assert response.status_code == 200
    expected_data = [doc.copy() for doc in mock_mongo_collection._mock_data]
    assert response.json() == expected_data

    mock_mongo_collection.find.assert_called_once_with({})


def test_get_recipes_with_name_filter_found(test_client, mock_mongo_collection):
    name_to_filter = "Milk Shake de Banana"
    response = test_client.get(f"/recipe/getRecipes?name={name_to_filter}")

    assert response.status_code == 200

    expected_data = []
    for doc in mock_mongo_collection._mock_data:
        if doc["Nome"] == name_to_filter:
            expected_data.append(doc.copy())

    assert response.json() == expected_data
    assert len(response.json()) == 1
    mock_mongo_collection.find.assert_called_once_with({"Nome": name_to_filter})


def test_get_recipes_with_name_filter_not_found(test_client, mock_mongo_collection):
    name_to_filter = "Sopa de Trollface"
    response = test_client.get(f"/recipe/getRecipes?name={name_to_filter}")

    assert response.status_code == 200
    assert response.json() == []

    mock_mongo_collection.find.assert_called_once_with({"Nome": name_to_filter})

def test_get_recipes_empty_collection(test_client, mock_mongo_collection):
    original_data = mock_mongo_collection._mock_data.copy()
    mock_mongo_collection._mock_data.clear()

    response = test_client.get("/recipe/getRecipes")

    assert response.status_code == 200
    assert response.json() == []

    mock_mongo_collection.find.assert_called_once_with({})

    mock_mongo_collection._mock_data.extend(original_data)