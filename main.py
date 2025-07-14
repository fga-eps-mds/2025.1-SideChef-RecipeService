from fastapi import FastAPI
from recipe.routes.recipe_routes import router as recipe_router
from recipe.routes.ocr_routes import router as ocr_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipe_router)
app.include_router(ocr_router)

@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "running"}


