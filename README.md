# 🛒 Inventory Management System (CLI)

A simple command-line inventory management tool written in Python using object-oriented programming. This app allows users to manage products by adding, removing, restocking, and viewing inventory. It also calculates the total value of all items in stock.

---

## 📁 Project Structure

```

├── main.py # Entry point and user interface logic
├── product.py # Product class definition
├── inventory.py # Inventory class to manage products
├── utils.py # Utility function for reading JSON
├── products.json # Sample product data

```

---

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone or download this repository.
3. Run the program from the terminal:

```bash
python main.py
```

Follow the on-screen menu to interact with the inventory.

---

## 📦 Features

- ✅ Load products from a JSON file
- ✅ View all inventory items
- ✅ Add new products (with duplicate name check)
- ✅ Remove products by name
- ✅ Restock products by name
- ✅ Calculate total inventory value
- ✅ User-friendly command-line interface

---

## 🧠 Key Concepts Used

- Classes and objects
- Encapsulation with getters and setters
- Lists and object iteration
- File handling (JSON)
- Pattern matching with `match-case` (Python 3.10+)
- Modular Python code across files

---

## 🧪 Sample `products.json`

```json
{
  "products": [
    {
      "name": "laptop",
      "price": 89999.5,
      "quantity": 25
    },
    {
      "name": "mouse",
      "price": 1499.49,
      "quantity": 150
    }
  ]
}
```
