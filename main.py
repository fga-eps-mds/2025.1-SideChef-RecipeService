from fastapi import FastAPI
from recipe.routes.recipe import router as recipe_router
from recipe.routes.ocr import router as ocr_router


app = FastAPI()

app.include_router(recipe_router)
app.include_router(ocr_router)

@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "running"}


