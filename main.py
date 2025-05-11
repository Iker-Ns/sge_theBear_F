from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.existencias import router as existencias_router
from database.Database import Database

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(existencias_router, prefix="/api", tags=["existenciass"])

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/existencias", response_class=HTMLResponse)
async def existencias(request: Request):
    return templates.TemplateResponse(
        request=request, name="existencias.html"
    )