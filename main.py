from core.config_loader import settings
from fastapi import FastAPI
from recipe.routes.recipe import router as recipe_router
from recipe.routes.ocr import router as ocr_router

# Middlewares here!
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    settings.FRONTEND_CORS_ORIGINS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipe_router)
app.include_router(ocr_router)

@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "running"}


