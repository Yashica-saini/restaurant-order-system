
# Restaurant Menu Data (given)

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# Cart starts empty


cart = []

# Function to display the cart


def print_cart():
    print("\nCurrent Cart:")

    if len(cart) == 0:
        print("Cart is empty")
        return

    for entry in cart:
        print(f"{entry['item']}  x{entry['quantity']}  Rs.{entry['price']}")


# Function to add items to cart


def add_to_cart(item_name, quantity):
    # Check if item exists
    if item_name not in menu:
        print("Item does not exist in menu")
        return

    # Check availability
    if not menu[item_name]["available"]:
        print("Item exists but is currently unavailable")
        return

    # Check if already in cart
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"Quantity updated for {item_name}")
            return

    # Add new item to cart
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })

    print(f"{item_name} added to cart")



# Function to remove item


def remove_from_cart(item_name):

    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"{item_name} removed from cart")
            return

    print("Item not found in cart")

# Function to update quantity


def update_quantity(item_name, quantity):

    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = quantity
            print(f"Quantity updated for {item_name}")
            return

    print("Item not found in cart")



# Simulating the required sequence


add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)   # should update quantity
print_cart()

add_to_cart("Mystery Burger", 1)  # does not exist
print_cart()

add_to_cart("Chicken Wings", 1)   # unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()



# Final Order Summary


print("\n========== Order Summary ==========")

subtotal = 0

for entry in cart:
    item_total = entry["quantity"] * entry["price"]
    subtotal += item_total

    print(f"{entry['item']:<15} x{entry['quantity']}    Rs.{item_total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:            Rs.{subtotal:.2f}")
print(f"GST (5%):            Rs.{gst:.2f}")
print(f"Total Payable:       Rs.{total:.2f}")
print("====================================")