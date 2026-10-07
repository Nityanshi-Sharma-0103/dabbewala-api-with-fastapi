# 🍱 Dabbawala Delivery API

A RESTful API built with **FastAPI**, **SQLModel**, and **SQLite** for managing dabbawala food-delivery orders, tracking order statuses, and generating daily order statistics.

This project was built to practice backend API development, database integration, request validation, query parameters, filtering, pagination, and interactive API documentation with Swagger/OpenAPI.

---

## 🚀 Features

- Create new delivery orders
- List delivery orders
- Filter orders by status
- Filter orders by creation date
- Pagination using `skip` and `limit`
- Track order status
- Generate daily order statistics
- SQLite database integration
- SQLModel ORM
- Automatic database table creation
- FastAPI dependency injection
- Interactive Swagger/OpenAPI documentation
- Health-check endpoint

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **SQLModel**
- **SQLite**
- **Uvicorn**
- **Git & GitHub**

---

## 📁 Project Structure

```text
dabbewala-api-with-fastapi/
│
├── images/
│   ├── screenshot1.png
│   ├── screenshot2.png
│   ├── screenshot3.png
│   ├── screenshot4.png
│   └── screenshot5.png
│
├── routes/
│   ├── __init__.py
│   ├── orders.py
│   └── stats.py
│
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── .gitignore
└── README.md
