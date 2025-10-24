# 📘 YumBook API Reference

Comprehensive REST API documentation for the YumBook Recipe App.

---

## 🔑 Authentication

All recipe endpoints require token authentication.

Include this header in all authorized requests:
Authorization: Token <your_token>



## 👤 Accounts API

### 1. Register
**POST** `/accounts/api/register/`

**Body:**
```json```
{
  "username": "newuser",
  "email": "user@example.com",
  "password": "strongpassword123"
}

Response (201):
```json```
{
  "id": 1,
  "username": "newuser",
  "email": "user@example.com"
}

### 2. Login
POST /accounts/api/login/

Body:

```json```
{
  "username": "newuser",
  "password": "strongpassword123"
}
Response (200):

```json```
{
  "token": "abcdef123456...",
  "user": {
    "id": 1,
    "username": "newuser",
    "email": "user@example.com"
  }
}


### 3. Logout
POST /accounts/api/logout/

Header:

Authorization: Token <your_token>
Response (200):

```json```
{
  "message": "Logged out successfully"
}


## 🍲 Recipe API
All recipe endpoints are under:

/recipes/api/recipes/

### 1. List Recipes
GET /recipes/api/recipes/

Response:

```json```
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Lasagna",
      "category": "Italian",
      "prep_time": "00:30:00",
      "cook_time": "01:00:00",
      "servings": 4
    }
  ]
}
### 2. Create Recipe
POST /recipes/api/recipes/

Body:

```json```
{
  "title": "Chocolate Cake",
  "instructions": "Mix, bake, and enjoy.",
  "prep_time": "00:20:00",
  "cook_time": "00:40:00",
  "category": "Dessert",
  "servings": 8
}
Response (201):

json

{
  "id": 2,
  "title": "Chocolate Cake",
  "category": "Dessert",
  "servings": 8
}
3. Retrieve a Single Recipe
GET /recipes/api/recipes/<id>/

Response:

json

{
  "id": 1,
  "title": "Lasagna",
  "instructions": "Layer pasta, sauce, and cheese...",
  "prep_time": "00:30:00",
  "cook_time": "01:00:00",
  "category": "Italian",
  "servings": 4
}
4. Update Recipe
PUT/PATCH /recipes/api/recipes/<id>/

Body:

json

{
  "title": "Vegetarian Lasagna",
  "category": "Italian",
  "cook_time": "01:10:00"
}
Response (200):

json

{
  "id": 1,
  "title": "Vegetarian Lasagna",
  "cook_time": "01:10:00"
}
### 5. Delete Recipe
DELETE /recipes/api/recipes/<id>/

Response (204):


### 6. Search and Ordering
Query Parameters:

swift
Copy code
GET /recipes/api/recipes/?search=lasagna
GET /recipes/api/recipes/?ordering=prep_time
GET /recipes/api/recipes/?ordering=-cook_time

### 7. Pagination
Each list response includes:

json
Copy code
{
  "count": 20,
  "next": "http://127.0.0.1:8000/recipes/api/recipes/?page=2",
  "previous": null,
  "results": [...]
}
⚠️ Validation & Error Handling
Duration Fields
If you submit an invalid prep_time or cook_time, you’ll get a clear message:

json
Copy code
{
  "cook_time": ["Invalid format for cook_time. Use 'HH:MM:SS' or total minutes (e.g. '00:30:00' or '30')."]
}
Auth Errors
json
Copy code
{
  "detail": "Authentication credentials were not provided."
}
Permission Errors
json
Copy code
{
  "detail": "You do not have permission to perform this action."
}
🧪 Example Workflow (Using Postman)
Register → /accounts/api/register/

Login → /accounts/api/login/ → copy token

Create Recipe → /recipes/api/recipes/ (Header: Authorization: Token <token>)

List Recipes → /recipes/api/recipes/

Logout → /accounts/api/logout/

🧾 License
MIT License © 2025 YumBook created by Omonye Omonlumhen


