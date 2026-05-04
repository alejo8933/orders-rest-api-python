from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import *
from app.routers import health_router, customers_router, products_router, orders_router, order_items_router

# Crea todas las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Orders API", version="1.0.0",
              docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(health_router, prefix="/api/v1")
app.include_router(customers_router, prefix="/api/v1")
app.include_router(products_router, prefix="/api/v1")
app.include_router(orders_router, prefix="/api/v1")
app.include_router(order_items_router, prefix="/api/v1")