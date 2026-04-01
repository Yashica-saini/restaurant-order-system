
# Sales Log Data (given)
sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],             "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],          "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],       "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# 1. Total revenue per day

print("\nRevenue Per Day")

daily_revenue = {}

for date, orders in sales_log.items():

    total = 0

    for order in orders:
        total += order["total"]

    daily_revenue[date] = total
    print(date, ":", "Rs.", total)


# 2. Best-selling day

best_day = None
highest_revenue = 0

for date, revenue in daily_revenue.items():

    if revenue > highest_revenue:
        highest_revenue = revenue
        best_day = date

print("\nBest Selling Day:", best_day, "with revenue Rs.", highest_revenue)


# 3. Most ordered item


item_count = {}

for date, orders in sales_log.items():

    for order in orders:

        for item in order["items"]:

            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1


most_ordered_item = None
highest_count = 0

for item, count in item_count.items():

    if count > highest_count:
        highest_count = count
        most_ordered_item = item

print("\nMost Ordered Item:", most_ordered_item, "-", highest_count, "orders")

# 4. Add new day to sales_log


sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nNew day added to sales log.\n")

# Recalculate revenue per day


print("Updated Revenue Per Day")

daily_revenue = {}

for date, orders in sales_log.items():

    total = 0

    for order in orders:
        total += order["total"]

    daily_revenue[date] = total
    print(date, ":", "Rs.", total)



# Recalculate best-selling day


best_day = None
highest_revenue = 0

for date, revenue in daily_revenue.items():

    if revenue > highest_revenue:
        highest_revenue = revenue
        best_day = date

print("\nUpdated Best Selling Day:", best_day, "with revenue Rs.", highest_revenue)



# 5. Print all orders using enumerate


print("\nNumbered Order List")

order_number = 1

for date, orders in sales_log.items():

    for order in orders:

        items_list = ", ".join(order["items"])

        print(f"{order_number}. [{date}] Order #{order['order_id']} — Rs.{order['total']} — Items: {items_list}")

        order_number += 1