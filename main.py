from fastapi import FastAPI
from recipe.routes.recipe import router
from models import Recipe
from db import get_db
from typing import List, Optional

app = FastAPI()

app.include_router(router)


@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "running"}


