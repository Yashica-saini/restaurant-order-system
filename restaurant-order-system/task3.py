
# Import copy module
import copy

# Inventory data (given)

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# Final cart from Task 2

cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# Create deep copy backup

inventory_backup = copy.deepcopy(inventory)

print("Backup created using deep copy.\n")


# Demonstrate deep copy works

print("Changing stock of Paneer Tikka in inventory...\n")

inventory["Paneer Tikka"]["stock"] = 5

print("Current inventory stock:", inventory["Paneer Tikka"]["stock"])
print("Backup inventory stock:", inventory_backup["Paneer Tikka"]["stock"])

# restore original value before continuing
inventory["Paneer Tikka"]["stock"] = inventory_backup["Paneer Tikka"]["stock"]

print("\nInventory restored to original state.\n")


# Simulate order fulfilment

print("Processing order from cart...\n")

for entry in cart:

    item_name = entry["item"]
    quantity_needed = entry["quantity"]

    if item_name in inventory:

        available_stock = inventory[item_name]["stock"]

        if available_stock >= quantity_needed:
            inventory[item_name]["stock"] -= quantity_needed

        else:
            print(f"Warning: Not enough stock for {item_name}")
            print(f"Only {available_stock} available, deducting remaining stock")

            inventory[item_name]["stock"] = 0



# Reorder alert check

print("\nChecking for reorder alerts...\n")

for item, details in inventory.items():

    stock = details["stock"]
    reorder_level = details["reorder_level"]

    if stock <= reorder_level:
        print(f"Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder_level})")


# Print final inventory

print("\nUpdated Inventory:")

for item, details in inventory.items():
    print(item, ":", details)

# Print backup inventory
print("\nInventory Backup (original copy):")

for item, details in inventory_backup.items():
    print(item, ":", details)