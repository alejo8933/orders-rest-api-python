import json
import os
from datetime import datetime
from app.database import SessionLocal, engine, Base
from app.models import Supplier, Product, Customer, Order, OrderItem

def run_seed():
    print("Iniciando carga de datos...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        json_path = os.path.join(os.path.dirname(__file__), "Orders.json")
        if not os.path.exists(json_path):
            print("No se encontró Orders.json, saltando seed.")
            return

        with open(json_path, "r", encoding="utf-8") as f:
            orders_data = json.load(f)
            
        suppliers = {}
        customers = {}
        products = {}
        
        for order in orders_data:
            c = order["customer"]
            if c["id"] not in customers:
                customers[c["id"]] = c
                
            for item in order["items"]:
                p = item["product"]
                if p["id"] not in products:
                    products[p["id"]] = p
                    
                s = p["supplier"]
                if s["id"] not in suppliers:
                    suppliers[s["id"]] = s
                    
        print("Insertando suppliers...")
        for s_id, s in suppliers.items():
            if not db.query(Supplier).filter(Supplier.id == s_id).first():
                db.add(Supplier(**s))
                
        print("Insertando customers...")
        for c_id, c in customers.items():
            if not db.query(Customer).filter(Customer.id == c_id).first():
                db.add(Customer(**c))
                
        print("Insertando products...")
        for p_id, p in products.items():
            if not db.query(Product).filter(Product.id == p_id).first():
                p_data = {k: v for k, v in p.items() if k != "supplier"}
                p_data["supplierId"] = p["supplier"]["id"]
                db.add(Product(**p_data))
                
        db.flush()
        
        print("Insertando orders y order items...")
        for o in orders_data:
            if not db.query(Order).filter(Order.id == o["id"]).first():
                order_date = datetime.fromisoformat(o["orderDate"]).date()
                new_order = Order(
                    id=o["id"],
                    orderDate=order_date,
                    orderNumber=o["orderNumber"],
                    customerId=o["customer"]["id"],
                    totalAmount=o["totalAmount"]
                )
                db.add(new_order)
                db.flush()
                
                for item in o["items"]:
                    if not db.query(OrderItem).filter(OrderItem.id == item["id"]).first():
                        new_item = OrderItem(
                            id=item["id"],
                            orderId=new_order.id,
                            productId=item["product"]["id"],
                            unitPrice=item["unitPrice"],
                            quantity=item["quantity"]
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
    run_seed()
