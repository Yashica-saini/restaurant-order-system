# menu data given in the assignment
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price": 40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price": 90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price": 80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# categories for grouping
categories = ["Starters", "Mains", "Desserts"]
print("Restaurant Menu\n")

# printing menu grouped by category
for category in categories:
    print(f"===== {category} =====")
    for item, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            if details["available"]:
                status = "Available"
            else:
                status = "Unavailable"
            print(f"{item:<15} {price:.2f}   [{status}]")
    print()

# total number of menu items
total_items = len(menu)
print("Total items on menu:", total_items)

# count available items
available_count = 0
for item in menu:
    if menu[item]["available"]:
        available_count += 1

print("Total available items:", available_count)


# most expensive item
most_expensive_item = ""
highest_price = 0

for item, details in menu.items():

    if details["price"] > highest_price:

        highest_price = details["price"]
        most_expensive_item = item

print("Most expensive item:", most_expensive_item, "- ", highest_price)

# items priced under 150
print("\nItems under 150:")
for item, details in menu.items():
    if details["price"] < 150:
        print(f"{item} - {details['price']}")