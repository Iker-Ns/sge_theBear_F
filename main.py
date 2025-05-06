from fastapi import FastAPI
from routers.restaurante import router as restaurante_router

app = FastAPI()

app.include_router(restaurante_router, prefix="/resturantes", tags=["restaurantes"]) 