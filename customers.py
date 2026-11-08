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
