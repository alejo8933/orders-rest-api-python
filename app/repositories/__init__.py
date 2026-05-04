from .supplier_repository import SupplierRepository
from .customer_repository import CustomerRepository
from .product_repository import ProductRepository
from .order_repository import OrderRepository
from .order_item_repository import OrderItemRepository

supplier_repository = SupplierRepository()
customer_repository = CustomerRepository()
product_repository = ProductRepository()
order_repository = OrderRepository()
order_item_repository = OrderItemRepository()
