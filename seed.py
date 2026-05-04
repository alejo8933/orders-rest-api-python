from datetime import date
from app.database import SessionLocal, engine, Base
from app.models import Supplier, Product, Customer, Order, OrderItem

Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    try:
        # Suppliers
        suppliers_data = [
            {"id": 1, "companyName": "Andes Coffee Export", "contactName": "Laura Méndez", "contactTitle": "Sales Manager", "city": "Medellín", "country": "Colombia", "phone": "+57 604 555 1200", "fax": None},
            {"id": 2, "companyName": "Cacao del Pacífico", "contactName": "Andrés Salazar", "contactTitle": "Account Executive", "city": "Cali", "country": "Colombia", "phone": "+57 602 555 8821", "fax": None},
            {"id": 3, "companyName": "Mediterranean Foods Ltd.", "contactName": "Elena Rossi", "contactTitle": "Export Director", "city": "Barcelona", "country": "España", "phone": "+34 93 555 7821", "fax": "+34 93 555 7822"},
            {"id": 4, "companyName": "Altiplano Grains", "contactName": "Sofía Quispe", "contactTitle": "Operations Lead", "city": "Puno", "country": "Perú", "phone": "+51 51 555 3300", "fax": None},
            {"id": 5, "companyName": "Sabores Andinos", "contactName": "Paula Rojas", "contactTitle": "Commercial Manager", "city": "Bogotá", "country": "Colombia", "phone": "+57 601 555 7610", "fax": None},
            {"id": 6, "companyName": "Asia Tea Traders", "contactName": "Kenji Nakamura", "contactTitle": "Regional Sales Dir.", "city": "Tokyo", "country": "Japón", "phone": "+81 3 5555 9080", "fax": "+81 3 5555 9081"},
            {"id": 7, "companyName": "La Mancha Dairy Co.", "contactName": "Javier Martín", "contactTitle": "Sales Representative", "city": "Toledo", "country": "España", "phone": "+34 925 555 210", "fax": None},
            {"id": 8, "companyName": "Fuego Maya Foods", "contactName": "Ricardo Castillo", "contactTitle": "Founder", "city": "Mérida", "country": "México", "phone": "+52 999 555 4400", "fax": None},
            {"id": 9, "companyName": "Pampa Dulce S.A.", "contactName": "Martín Acosta", "contactTitle": "Key Account Manager", "city": "Buenos Aires", "country": "Argentina", "phone": "+54 11 5555 1930", "fax": None},
            {"id": 10, "companyName": "Iberian Select Foods", "contactName": "Clara Domínguez", "contactTitle": "International Sales", "city": "Madrid", "country": "España", "phone": "+34 91 555 6540", "fax": "+34 91 555 6541"}
        ]
        for s in suppliers_data:
            if not db.query(Supplier).filter(Supplier.id == s["id"]).first():
                db.add(Supplier(**s))

        # Products
        products_data = [
            {"id": 1, "productName": "Café Colombiano Premium", "supplierId": 1, "unitPrice": 24.90, "package": "Caja x 500g", "isDiscontinued": False},
            {"id": 2, "productName": "Chocolate Orgánico 70%", "supplierId": 2, "unitPrice": 40.00, "package": "Caja x 12 unidades", "isDiscontinued": False},
            {"id": 3, "productName": "Aceite de Oliva E. Virgen", "supplierId": 3, "unitPrice": 28.50, "package": "Botella 750ml", "isDiscontinued": False},
            {"id": 4, "productName": "Quinua Blanca Orgánica", "supplierId": 4, "unitPrice": 18.00, "package": "Bolsa x 1kg", "isDiscontinued": False},
            {"id": 5, "productName": "Mermelada de Mora", "supplierId": 5, "unitPrice": 22.00, "package": "Frasco 250g", "isDiscontinued": False},
            {"id": 6, "productName": "Té Verde Sencha", "supplierId": 6, "unitPrice": 12.00, "package": "Caja x 20 sobres", "isDiscontinued": False},
            {"id": 7, "productName": "Queso Manchego Curado", "supplierId": 7, "unitPrice": 35.00, "package": "Pieza 500g", "isDiscontinued": False},
            {"id": 8, "productName": "Salsa Picante Artesanal", "supplierId": 8, "unitPrice": 9.90, "package": "Botella 150ml", "isDiscontinued": False},
            {"id": 9, "productName": "Dulce de Leche Clásico", "supplierId": 9, "unitPrice": 16.00, "package": "Frasco 400g", "isDiscontinued": False},
            {"id": 10, "productName": "Jamón Serrano Reserva", "supplierId": 10, "unitPrice": 45.00, "package": "Paquete 250g", "isDiscontinued": False}
        ]
        for p in products_data:
            if not db.query(Product).filter(Product.id == p["id"]).first():
                db.add(Product(**p))

        # Customers
        customers_data = [
            {"id": 1, "firstName": "Carlos", "lastName": "Ramírez", "city": "Bogotá", "country": "Colombia", "phone": "+57 300 123 4567"},
            {"id": 2, "firstName": "María", "lastName": "González", "city": "Quito", "country": "Ecuador", "phone": "+593 99 222 3344"},
            {"id": 3, "firstName": "Diego", "lastName": "Fernández", "city": "Lima", "country": "Perú", "phone": "+51 987 654 321"},
            {"id": 4, "firstName": "Ana", "lastName": "Torres", "city": "Santiago", "country": "Chile", "phone": "+56 9 8765 4321"},
            {"id": 5, "firstName": "Lucía", "lastName": "Morales", "city": "Ciudad de México", "country": "México", "phone": "+52 55 1234 5678"},
            {"id": 6, "firstName": "Jorge", "lastName": "Pineda", "city": "San José", "country": "Costa Rica", "phone": "+506 8888 1122"},
            {"id": 7, "firstName": "Valentina", "lastName": "Herrera", "city": "Montevideo", "country": "Uruguay", "phone": "+598 91 234 567"},
            {"id": 8, "firstName": "Pedro", "lastName": "Castillo", "city": "Panamá", "country": "Panamá", "phone": "+507 6000 7788"},
            {"id": 9, "firstName": "Camila", "lastName": "Silva", "city": "São Paulo", "country": "Brasil", "phone": "+55 11 99999 2233"},
            {"id": 10, "firstName": "Santiago", "lastName": "Vega", "city": "Buenos Aires", "country": "Argentina", "phone": "+54 9 11 2345 6789"}
        ]
        for c in customers_data:
            if not db.query(Customer).filter(Customer.id == c["id"]).first():
                db.add(Customer(**c))

        # Orders & Items
        orders_data = [
            {"orderNumber": "ORD-1001", "customerId": 1, "orderDate": date(2026, 4, 1), "items": [{"p": 1, "q": 2, "price": 24.90}, {"p": 2, "q": 2, "price": 40.00}], "total": 129.80},
            {"orderNumber": "ORD-1002", "customerId": 2, "orderDate": date(2026, 4, 2), "items": [{"p": 3, "q": 3, "price": 28.50}], "total": 85.50},
            {"orderNumber": "ORD-1003", "customerId": 3, "orderDate": date(2026, 4, 3), "items": [{"p": 4, "q": 5, "price": 18.00}, {"p": 5, "q": 3, "price": 22.00}], "total": 156.00},
            {"orderNumber": "ORD-1004", "customerId": 4, "orderDate": date(2026, 4, 4), "items": [{"p": 6, "q": 6, "price": 12.00}], "total": 72.00},
            {"orderNumber": "ORD-1005", "customerId": 5, "orderDate": date(2026, 4, 5), "items": [{"p": 7, "q": 6, "price": 35.00}], "total": 210.00},
            {"orderNumber": "ORD-1006", "customerId": 6, "orderDate": date(2026, 4, 6), "items": [{"p": 8, "q": 10, "price": 9.90}], "total": 99.00},
            {"orderNumber": "ORD-1007", "customerId": 7, "orderDate": date(2026, 4, 7), "items": [{"p": 9, "q": 4, "price": 16.00}], "total": 64.00},
            {"orderNumber": "ORD-1008", "customerId": 8, "orderDate": date(2026, 4, 8), "items": [{"p": 10, "q": 4, "price": 45.00}], "total": 180.00},
            {"orderNumber": "ORD-1009", "customerId": 9, "orderDate": date(2026, 4, 9), "items": [{"p": 4, "q": 3, "price": 18.00}], "total": 54.00},
            {"orderNumber": "ORD-1010", "customerId": 10, "orderDate": date(2026, 4, 10), "items": [{"p": 1, "q": 4, "price": 24.90}, {"p": 8, "q": 2, "price": 9.90}], "total": 119.40}
        ]
        
        for o in orders_data:
            if not db.query(Order).filter(Order.orderNumber == o["orderNumber"]).first():
                new_order = Order(
                    orderDate=o["orderDate"],
                    orderNumber=o["orderNumber"],
                    customerId=o["customerId"],
                    totalAmount=o["total"]
                )
                db.add(new_order)
                db.flush()
                
                for item in o["items"]:
                    new_item = OrderItem(
                        orderId=new_order.id,
                        productId=item["p"],
                        unitPrice=item["price"],
                        quantity=item["q"]
                    )
                    db.add(new_item)
        
        db.commit()
        print("Database seeded successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
