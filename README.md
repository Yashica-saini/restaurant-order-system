# Restaurant Order Management System

## Overview

This project is a simple **Restaurant Order Management System** implemented in Python.
The goal of the project is to practice using Python's core data structures such as **lists, dictionaries, and nested dictionaries**.

The system simulates basic restaurant operations including:

* Exploring a restaurant menu
* Managing a customer's cart
* Tracking inventory
* Analyzing daily sales data

All tasks were implemented using basic Python concepts without using external libraries (except `copy` for deep copy).

---

## Features

### Task 1 – Menu Exploration

* Display the restaurant menu grouped by category.
* Count the total number of menu items.
* Count how many items are currently available.
* Identify the most expensive menu item.
* Display items priced under a certain value.

### Task 2 – Cart Operations

* Add items to the cart.
* Prevent duplicate cart entries by updating quantity.
* Handle unavailable or non-existent menu items.
* Remove items from the cart.
* Generate an order summary including subtotal, GST, and total payable.

### Task 3 – Inventory Tracker

* Use **deep copy** to create a backup of the inventory.
* Demonstrate that modifying the main inventory does not affect the backup.
* Deduct stock based on customer orders.
* Prevent stock values from going below zero.
* Generate reorder alerts when stock reaches the reorder level.

### Task 4 – Sales Log Analysis

* Calculate total revenue for each day.
* Identify the best-selling day.
* Determine the most frequently ordered item.
* Update the sales log with new orders and recompute statistics.
* Display all orders in a numbered format using `enumerate`.

---

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Nested Data Structures
* Loops and Conditionals

---



---

## How to Run

1. Make sure Python is installed on your system.
2. Download or clone this repository.
3. Run the script using:

```
python part2_order_system.py
```

---

## Learning Outcome

This project helped reinforce concepts such as:

* Working with complex data structures
* Data manipulation using loops and conditionals
* Writing modular and readable Python code
* Performing basic data analysis using dictionaries

---

## Author
Yashica Saini

