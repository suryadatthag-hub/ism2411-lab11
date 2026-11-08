# ISM2411 Lab 11 - Customer Dictionary & Lookup

# Exercise 1: One customer
print("Exercise 1: One customer")
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
print("\nExercise 2: Update and add")
customer["phone"] = "555-0101"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print("\nExercise 3: Safe lookup")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error} - the email field was deleted.")

# Exercise 4: Iterate
print("\nExercise 4: Iterate")
for key, value in customer.items():
    print(f"{key}: {value}")

# .items() gives both the key and value; a plain loop gives only the keys.
print("Keys from iterating without .items():")
for key in customer:
    print(key)

# Exercise 5: Lookup table
print("\nExercise 5: Lookup table")
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
print("\nExercise 6: List of dicts")
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
print("\nExercise 7: Nested catalog")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")

# Exercise 8: Sales by region
print("\nExercise 8: Sales by region")
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
