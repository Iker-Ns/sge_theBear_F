from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.cuenta import router as cuenta_router
from routers.restaurante import router as restaurante_router
from routers.trabajador import router as trabajador_router
from routers.producto_cuenta import router as producto_cuenta_router
from database.Database import Database

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(restaurante_router, prefix="/api", tags=["restaurantes"])
app.include_router(trabajador_router, prefix="/api", tags=["trabajadores"])
app.include_router(cuenta_router, prefix="/api", tags=["cuentas"])
app.include_router(producto_cuenta_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    return templates.TemplateResponse(
        request=request, name="client.html"
    )

@app.get("/restaurant", response_class=HTMLResponse)
async def restaurant(request: Request):
    return templates.TemplateResponse(
        request=request, name="restaurant.html"
    )

@app.get("/trabajadores", response_class=HTMLResponse)
async def trabajador(request: Request):
    return templates.TemplateResponse(
        request=request, name="trabajador.html"
    )
      
@app.get("/cuenta", response_class=HTMLResponse)
async def cuenta(request: Request):
    return templates.TemplateResponse(
        request=request, name="cuenta.html"
    )