"""
Utility functions for the inventory system.
Also has many problems - duplicated logic, no validation, poor patterns.
"""

import json
import os
from datetime import datetime


# BAD: Duplicates the load/save logic from inventory.py
DATA_FILE = "inventory_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"products": [], "orders": [], "suppliers": [], "categories": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


def format_price(price):
    return "$" + str(round(price, 2))


def format_date(date_str):
    # BAD: Fragile date parsing
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        return dt.strftime("%m/%d/%Y")
    except:
        return date_str


def validate_email(email):
    # BAD: Terrible email validation
    if "@" in email and "." in email:
        return True
    return False


def validate_phone(phone):
    # BAD: Only works for specific format
    if len(phone) == 10 and phone.isdigit():
        return True
    return False


def calculate_tax(amount, rate=0.08):
    return amount * rate


def apply_bulk_discount(total, quantity):
    # BAD: Magic numbers everywhere
    if quantity >= 100:
        return total * 0.85
    elif quantity >= 50:
        return total * 0.90
    elif quantity >= 20:
        return total * 0.95
    return total


def export_to_csv(data, filename):
    # BAD: Manual CSV generation (should use csv module)
    if not data:
        return

    f = open(filename, "w")
    # Write header
    headers = list(data[0].keys())
    f.write(",".join(headers) + "\n")

    # Write rows
    for item in data:
        row = []
        for h in headers:
            val = str(item.get(h, ""))
            # BAD: Doesn't handle commas in values
            row.append(val)
        f.write(",".join(row) + "\n")

    f.close()


def import_from_csv(filename):
    # BAD: Manual CSV parsing (should use csv module)
    if not os.path.exists(filename):
        return []

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    if len(lines) < 2:
        return []

    headers = lines[0].strip().split(",")
    results = []
    for line in lines[1:]:
        values = line.strip().split(",")
        item = {}
        for i in range(len(headers)):
            if i < len(values):
                item[headers[i]] = values[i]
        results.append(item)

    return results


def generate_sku(category, product_id):
    # BAD: Simple SKU generation with no collision checking
    cat_code = category[:3].upper()
    return f"{cat_code}-{product_id:05d}"


def calculate_reorder_point(avg_daily_sales, lead_time_days, safety_stock=0):
    return (avg_daily_sales * lead_time_days) + safety_stock


def get_product_age_days(created_date_str):
    # BAD: Fragile date handling
    try:
        created = datetime.strptime(created_date_str, "%Y-%m-%d %H:%M:%S.%f")
        delta = datetime.now() - created
        return delta.days
    except:
        return 0


def sort_products_by_value(products):
    # BAD: Custom bubble sort instead of using sorted()
    items = list(products)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = items[j]["price"] * items[j]["qty"]
            val2 = items[j + 1]["price"] * items[j + 1]["qty"]
            if val1 < val2:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def check_stock_alerts(products):
    alerts = []
    for p in products:
        if p["qty"] <= 0:
            alerts.append({"product": p["name"], "type": "OUT_OF_STOCK", "severity": "critical"})
        elif p["qty"] < p.get("min_stock", 10):
            alerts.append({"product": p["name"], "type": "LOW_STOCK", "severity": "warning"})
        elif p["qty"] > p.get("max_stock", 1000):
            alerts.append({"product": p["name"], "type": "OVERSTOCK", "severity": "info"})
    return alerts
