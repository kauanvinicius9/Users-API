# CRUD

A lightweight REST API built with **FastAPI** to demonstrate user management fundamentals. The project focuses on clean architecture, request validation, and RESTful design without introducing database complexity.

## Features

* RESTful CRUD operations
* Automatic request validation with Pydantic
* Automatic OpenAPI/Swagger documentation
* In-memory data storage
* Clean project structure

## Tech Stack

* Python;
* FastAPI;

## Endpoints

| METHOD | ENDPOINT | DESCRIPTION |
| ------ | ------------- | ----------------------- |
| GET    | `/users`      | List all users          |
| GET    | `/users/{id}` | Retrieve a user by ID   |
| POST   | `/users`      | Create a new user       |
| PUT    | `/users/{id}` | Update an existing user |
| DELETE | `/users/{id}` | Remove a user           |

## Architecture Back-End

```
app/
├── main.py
├── routers/
├── services/
├── schemas/
└── db/
```

* **routers** → API endpoints
* **services** → Business logic
* **schemas** → Request and response models
* **database** → In-memory data source (temporary)

## Notes

This project intentionally uses an in-memory dataset to keep the focus on API design and FastAPI fundamentals. The architecture is organized to allow seamless migration to a persistent database layer with minimal code changes.

## Running

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```bash
http://localhost:8000/docs
```

ReDoc:

```bash
http://localhost:8000/redoc
```