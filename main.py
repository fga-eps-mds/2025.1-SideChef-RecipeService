from fastapi import FastAPI
from recipe.routes.recipe import router


app = FastAPI()

app.include_router(router)


@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "running"}


