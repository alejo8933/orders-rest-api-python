from .health import router as health_router
from .customers import router as customers_router
from .products import router as products_router
from .orders import router as orders_router
from .order_items import router as order_items_router

__all__ = [
    "health_router",
    "customers_router",
    "products_router",
    "orders_router",
    "order_items_router"
]
