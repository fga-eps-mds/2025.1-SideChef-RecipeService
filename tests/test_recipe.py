from typing import Dict

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