# Reflection
# 1. For optional data (customer email, for example), I would use `.get()` because
# it can give a default if that piece of data is not available. For required data,
# I would use bracket notation because if that specific key is not there, it should
# indicate an issue with the data. Basically, if the data being requested is likely
# to be missing, use `.get()` or if it should be addressed, use bracket notation.
#
# 2. Creating a summary as a dictionary makes me think of Excel SUMIF or a
# PivotTable - organizing data based on a category (region) and adding up the sales
# in that category. With Python, this could be automatically done across many files,
# and it could be consistently run every time new data is available. Additionally,
# Python can also handle bulk data by iterating through many rows without needing
# every row to be in a worksheet.

# ISM2411 Lab 11 - Customer Dictionary & Lookup

# Exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: Update and add
customer["phone"] = "555-0101"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error} - the email field was deleted.")

# Exercise 4: Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

# .items() gives both the key and value; a plain loop gives only the keys.
for key in customer:
    print(key)

# Exercise 5: Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15,
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: List of dicts
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 12400},
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8000},
]

purchase = 300
for person in customers:
    discount_rate = tier_discounts.get(person["tier"], 0)
    discount_amount = purchase * discount_rate
    print(f"{person['name']} | {person['tier']} | Discount: ${discount_amount:.2f}")

# Exercise 7: Nested catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")

# Exercise 8: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + transaction["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
