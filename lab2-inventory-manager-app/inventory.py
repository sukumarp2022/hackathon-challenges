"""
Legacy Inventory Management System
====================================
WARNING: This codebase was written hastily and has MANY issues.
Your job is to use GitHub Copilot to refactor, improve, and modernize it.

Known problems:
- God class / monolithic design
- No type hints
- Poor naming conventions
- Performance issues (inefficient loops, repeated computations)
- No error handling
- No separation of concerns
- Magic numbers and hardcoded values
- Security issues
"""

import json
import os
import time
from datetime import datetime


DATA_FILE = "inventory_data.json"


def load():
    if os.path.exists(DATA_FILE):
        f = open(DATA_FILE, "r")
        d = json.load(f)
        f.close()
        return d
    return {"products": [], "orders": [], "suppliers": [], "categories": []}


def save(d):
    f = open(DATA_FILE, "w")
    json.dump(d, f)
    f.close()


def add_product(name, price, qty, cat, sup):
    d = load()
    id = len(d["products"]) + 1
    p = {
        "id": id,
        "name": name,
        "price": price,
        "qty": qty,
        "cat": cat,
        "sup": sup,
        "created": str(datetime.now()),
        "updated": str(datetime.now()),
        "active": True,
        "discount": 0,
        "min_stock": 10,
        "max_stock": 1000,
    }
    d["products"].append(p)
    save(d)
    return p


def get_product(id):
    d = load()
    for p in d["products"]:
        if p["id"] == id:
            return p
    return None


def update_product(id, name=None, price=None, qty=None):
    d = load()
    for p in d["products"]:
        if p["id"] == id:
            if name:
                p["name"] = name
            if price:
                p["price"] = price
            if qty:
                p["qty"] = qty
            p["updated"] = str(datetime.now())
            save(d)
            return p
    return None


def delete_product(id):
    d = load()
    new_list = []
    for p in d["products"]:
        if p["id"] != id:
            new_list.append(p)
    d["products"] = new_list
    save(d)


def search_products(query):
    d = load()
    results = []
    for p in d["products"]:
        if query.lower() in p["name"].lower():
            results.append(p)
    return results


def get_products_by_category(cat):
    d = load()
    results = []
    for p in d["products"]:
        if p["cat"] == cat:
            results.append(p)
    return results


def get_low_stock():
    d = load()
    results = []
    for p in d["products"]:
        if p["qty"] < p["min_stock"]:
            results.append(p)
    return results


def calculate_inventory_value():
    d = load()
    total = 0
    for p in d["products"]:
        val = p["price"] * p["qty"]
        if p["discount"] > 0:
            val = val - (val * p["discount"] / 100)
        total = total + val
    return total


def get_inventory_report():
    d = load()
    report = {}
    report["total_products"] = len(d["products"])
    report["total_value"] = calculate_inventory_value()
    report["low_stock"] = len(get_low_stock())

    # BAD: Recalculates everything multiple times
    cat_counts = {}
    for p in d["products"]:
        if p["cat"] in cat_counts:
            cat_counts[p["cat"]] = cat_counts[p["cat"]] + 1
        else:
            cat_counts[p["cat"]] = 1
    report["by_category"] = cat_counts

    sup_counts = {}
    for p in d["products"]:
        if p["sup"] in sup_counts:
            sup_counts[p["sup"]] = sup_counts[p["sup"]] + 1
        else:
            sup_counts[p["sup"]] = 1
    report["by_supplier"] = sup_counts

    # BAD: N+1 style - loads data inside loop
    active_count = 0
    inactive_count = 0
    for p in d["products"]:
        if p["active"]:
            active_count = active_count + 1
        else:
            inactive_count = inactive_count + 1
    report["active"] = active_count
    report["inactive"] = inactive_count

    return report


def place_order(product_id, quantity, customer_name):
    d = load()
    product = None
    for p in d["products"]:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        return {"error": "Product not found"}

    if product["qty"] < quantity:
        return {"error": "Not enough stock"}

    # BAD: No transaction safety
    product["qty"] = product["qty"] - quantity

    order = {
        "id": len(d["orders"]) + 1,
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total_price": product["price"] * quantity,
        "customer": customer_name,
        "status": "pending",
        "created": str(datetime.now()),
    }

    # BAD: applying discount wrong - should apply before total
    if product["discount"] > 0:
        order["total_price"] = order["total_price"] - (
            order["total_price"] * product["discount"] / 100
        )
        order["discount_applied"] = product["discount"]

    d["orders"].append(order)
    save(d)
    return order


def get_order(id):
    d = load()
    for o in d["orders"]:
        if o["id"] == id:
            return o
    return None


def get_orders_by_customer(customer):
    d = load()
    results = []
    for o in d["orders"]:
        if o["customer"] == customer:
            results.append(o)
    return results


def update_order_status(id, status):
    d = load()
    for o in d["orders"]:
        if o["id"] == id:
            o["status"] = status
            save(d)
            return o
    return None


def get_sales_report():
    d = load()
    total_sales = 0
    total_orders = len(d["orders"])

    # BAD: Extremely inefficient - loads data multiple times
    for o in d["orders"]:
        total_sales = total_sales + o["total_price"]

    # BAD: Recounts everything per product
    product_sales = {}
    for o in d["orders"]:
        pid = o["product_id"]
        if pid in product_sales:
            product_sales[pid]["count"] = product_sales[pid]["count"] + 1
            product_sales[pid]["revenue"] = (
                product_sales[pid]["revenue"] + o["total_price"]
            )
        else:
            product_sales[pid] = {
                "name": o["product_name"],
                "count": 1,
                "revenue": o["total_price"],
            }

    # BAD: Sorting by iterating through all items multiple times
    sorted_products = []
    temp = list(product_sales.values())
    while len(temp) > 0:
        max_rev = -1
        max_item = None
        for item in temp:
            if item["revenue"] > max_rev:
                max_rev = item["revenue"]
                max_item = item
        sorted_products.append(max_item)
        temp.remove(max_item)

    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "top_products": sorted_products[:5],
    }


def add_supplier(name, contact, email, phone):
    d = load()
    s = {
        "id": len(d["suppliers"]) + 1,
        "name": name,
        "contact": contact,
        "email": email,
        "phone": phone,
    }
    d["suppliers"].append(s)
    save(d)
    return s


def add_category(name, description):
    d = load()
    c = {
        "id": len(d["categories"]) + 1,
        "name": name,
        "description": description,
    }
    d["categories"].append(c)
    save(d)
    return c


def get_all_categories():
    d = load()
    return d["categories"]


def get_all_suppliers():
    d = load()
    return d["suppliers"]


# BAD: This function does way too many things
def generate_full_report():
    print("=" * 60)
    print("INVENTORY MANAGEMENT SYSTEM - FULL REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now()}")
    print()

    d = load()

    print("--- PRODUCTS ---")
    for p in d["products"]:
        print(
            f"  [{p['id']}] {p['name']} - ${p['price']} x {p['qty']} units"
        )
        if p["qty"] < p["min_stock"]:
            print(f"       ⚠️  LOW STOCK! (min: {p['min_stock']})")

    print()
    print("--- ORDERS ---")
    for o in d["orders"]:
        print(
            f"  [{o['id']}] {o['product_name']} x{o['quantity']} "
            f"- ${o['total_price']} ({o['status']})"
        )

    print()
    print("--- INVENTORY VALUE ---")
    # BAD: recalculates everything again
    val = calculate_inventory_value()
    print(f"  Total Value: ${val}")

    print()
    print("--- SALES ---")
    # BAD: recalculates everything again
    sales = get_sales_report()
    print(f"  Total Sales: ${sales['total_sales']}")
    print(f"  Total Orders: {sales['total_orders']}")

    print()
    report = get_inventory_report()
    print("--- BY CATEGORY ---")
    for cat, count in report["by_category"].items():
        print(f"  {cat}: {count} products")

    print()
    print("--- LOW STOCK ALERTS ---")
    low = get_low_stock()
    for p in low:
        print(f"  ⚠️  {p['name']}: {p['qty']} remaining (min: {p['min_stock']})")

    print("=" * 60)


class InventoryApp:
    """Main CLI interface - also a mess"""

    def __init__(self):
        self.running = True

    def run(self):
        print("Welcome to Inventory Manager v0.1")
        while self.running:
            print("\n1. Add Product")
            print("2. View Products")
            print("3. Search Products")
            print("4. Place Order")
            print("5. View Orders")
            print("6. Inventory Report")
            print("7. Sales Report")
            print("8. Full Report")
            print("9. Add Supplier")
            print("10. Add Category")
            print("0. Exit")

            choice = input("\nChoice: ")

            if choice == "1":
                name = input("Product name: ")
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                cat = input("Category: ")
                sup = input("Supplier: ")
                p = add_product(name, price, qty, cat, sup)
                print(f"Product added: {p['name']} (ID: {p['id']})")

            elif choice == "2":
                d = load()
                for p in d["products"]:
                    print(
                        f"  [{p['id']}] {p['name']} - ${p['price']} "
                        f"({p['qty']} in stock)"
                    )

            elif choice == "3":
                q = input("Search: ")
                results = search_products(q)
                for p in results:
                    print(f"  [{p['id']}] {p['name']} - ${p['price']}")

            elif choice == "4":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                customer = input("Customer name: ")
                order = place_order(pid, qty, customer)
                if "error" in order:
                    print(f"Error: {order['error']}")
                else:
                    print(
                        f"Order placed: #{order['id']} - ${order['total_price']}"
                    )

            elif choice == "5":
                d = load()
                for o in d["orders"]:
                    print(
                        f"  [{o['id']}] {o['product_name']} x{o['quantity']} "
                        f"- ${o['total_price']} ({o['status']})"
                    )

            elif choice == "6":
                report = get_inventory_report()
                print(json.dumps(report, indent=2))

            elif choice == "7":
                report = get_sales_report()
                print(json.dumps(report, indent=2))

            elif choice == "8":
                generate_full_report()

            elif choice == "9":
                name = input("Supplier name: ")
                contact = input("Contact person: ")
                email = input("Email: ")
                phone = input("Phone: ")
                s = add_supplier(name, contact, email, phone)
                print(f"Supplier added: {s['name']}")

            elif choice == "10":
                name = input("Category name: ")
                desc = input("Description: ")
                c = add_category(name, desc)
                print(f"Category added: {c['name']}")

            elif choice == "0":
                self.running = False
                print("Goodbye!")

            else:
                print("Invalid choice!")


if __name__ == "__main__":
    app = InventoryApp()
    app.run()
