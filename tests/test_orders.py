import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models.customer import Customer
from app.models.product import Product
from app.models.supplier import Supplier

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    
    # Create test data
    if not db.query(Supplier).filter(Supplier.id == 1).first():
        supplier = Supplier(id=1, companyName="Test Supplier", contactName="Test", contactTitle="Test", city="Test", country="Test", phone="123")
        db.add(supplier)
        
    if not db.query(Customer).filter(Customer.id == 1).first():
        customer = Customer(id=1, firstName="Test", lastName="User", city="City", country="Country", phone="123")
        db.add(customer)
        
    if not db.query(Product).filter(Product.id == 1).first():
        product1 = Product(id=1, productName="Prod 1", supplierId=1, unitPrice=10.0, package="Box", isDiscontinued=False)
        db.add(product1)
        
    if not db.query(Product).filter(Product.id == 2).first():
        product2 = Product(id=2, productName="Prod 2", supplierId=1, unitPrice=20.0, package="Box", isDiscontinued=False)
        db.add(product2)
        
    db.commit()
    db.close()
    
    yield
    
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# 1. POST /api/v1/orders body válido → 201, totalAmount calculado
def test_create_order_valid():
    response = client.post("/api/v1/orders", json={
        "customerId": 1,
        "items": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 1}
        ]
    })
    assert response.status_code == 201
    data = response.json()
    assert data["totalAmount"] == 40.0 # 2*10.0 + 1*20.0
    assert data["customerId"] == 1
    assert "id" in data

# 2. POST /api/v1/orders customerId inexistente → 404
def test_create_order_invalid_customer():
    response = client.post("/api/v1/orders", json={
        "customerId": 999,
        "items": [
            {"productId": 1, "quantity": 1}
        ]
    })
    assert response.status_code == 404

# 3. GET /api/v1/orders/9999 → 404
def test_get_order_not_found():
    response = client.get("/api/v1/orders/9999")
    assert response.status_code == 404

# 4. GET /api/v1/orders?page=1&limit=5 → 200, campo "items" y "total" presentes
def test_get_orders_paginated():
    response = client.get("/api/v1/orders?page=1&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data

# 5. POST /api/v1/orders/{id}/items → 201, totalAmount recalculado
def test_add_order_item_recalculates_total():
    resp_order = client.post("/api/v1/orders", json={
        "customerId": 1,
        "items": [{"productId": 1, "quantity": 1}] # total = 10.0
    })
    order_id = resp_order.json()["id"]
    
    response = client.post(f"/api/v1/orders/{order_id}/items", json={
        "productId": 2,
        "quantity": 2 # 2 * 20.0 = 40.0
    })
    assert response.status_code == 201
    
    resp_order_check = client.get(f"/api/v1/orders/{order_id}")
    assert resp_order_check.json()["totalAmount"] == 50.0

# 6. PATCH /api/v1/orders/{id}/items/{itemId} → 200, totalAmount recalculado
def test_update_order_item_recalculates_total():
    resp_order = client.post("/api/v1/orders", json={
        "customerId": 1,
        "items": [{"productId": 1, "quantity": 2}] # total = 20.0
    })
    order_data = resp_order.json()
    order_id = order_data["id"]
    item_id = order_data["items"][0]["id"]
    
    response = client.patch(f"/api/v1/orders/{order_id}/items/{item_id}", json={
        "quantity": 5 # 5 * 10.0 = 50.0
    })
    assert response.status_code == 200
    
    resp_order_check = client.get(f"/api/v1/orders/{order_id}")
    assert resp_order_check.json()["totalAmount"] == 50.0

# 7. DELETE /api/v1/orders/{id}/items/{itemId} → 204
def test_delete_order_item_recalculates_total():
    resp_order = client.post("/api/v1/orders", json={
        "customerId": 1,
        "items": [
            {"productId": 1, "quantity": 2}, # 20.0
            {"productId": 2, "quantity": 1}  # 20.0
        ]
    })
    order_data = resp_order.json()
    order_id = order_data["id"]
    item_id = order_data["items"][0]["id"]
    
    response = client.delete(f"/api/v1/orders/{order_id}/items/{item_id}")
    assert response.status_code == 204
    
    resp_order_check = client.get(f"/api/v1/orders/{order_id}")
    assert resp_order_check.json()["totalAmount"] == 20.0

# 8. GET /api/v1/health → 200, {"status":"ok"}
def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
