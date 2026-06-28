# ============================================
# SALES REPORT GENERATOR
# Real use: E-commerce companies (Flipkart, Amazon)
# Garvit - Day 1 - python-grind/day1/07_sales_report.py
# ============================================




sales_data = [
    {"product": "Laptop",   "units": 5,  "price": 45000},
    {"product": "Phone",    "units": 12, "price": 18000},
    {"product": "Tablet",   "units": 3,  "price": 22000},
    {"product": "Earbuds",  "units": 20, "price": 2500},
    {"product": "Charger",  "units": 8,  "price": 1500},
]

print("=" * 40)
print("       MONTHLY SALES REPORT")
print("=" * 40)



# Teen alag loop mat banao — ek hi loop mein sab hoga
total_revenue = 0
best_revenue = 0
best_product = ""

for index, product in enumerate(sales_data, 1):
    product_revenue = product["units"] * product["price"]
    total_revenue += product_revenue  # += se add karte jao

    # best track karo
    if product_revenue > best_revenue:
        best_revenue = product_revenue
        best_product = product["product"]

    print(f"{index}. {product['product']:<10} → ₹{product_revenue:,}")

print("=" * 40)
print(f"Total Revenue : ₹{total_revenue}")
print(f"Best Product : {best_product}")



