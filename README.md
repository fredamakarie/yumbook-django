# 🍴 YumBook — Django Recipe App

**YumBook** is a Django-powered recipe management platform where users can register, log in, and manage their personal recipes.  
Each user has their own private collection — only accessible after authentication.  
Built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**, YumBook includes both HTML pages and a RESTful API.

---

## 🚀 Features

- ✅ User Registration, Login & Logout (HTML and API)
- ✅ Create, View, Update, and Delete Recipes
- ✅ Each user sees only **their own recipes**
- ✅ Token-based API Authentication
- ✅ Pagination and sorting for recipe listings
- ✅ Ingredient management for each recipe
- ✅ Clean validation for time/duration fields
- ✅ Admin interface for superusers

---

## 🧩 Tech Stack

Backend Framework -	Django 5.x
API Framework	- Django REST Framework
Authentication -	DRF Token Auth
Database	= postgreSQL
Frontend	- Django Templates (HTML, CSS, JS)
Media Storage	- Django File Storage (images in /media/)

## 🧩 Project Structure
yumbook_backend/
│
├── accounts/                   # User accounts & authentication
│   ├── urls.py                 #routes
│   ├── views.py
│   ├── serializers.py
│   ├── forms.py
│   └── templates/accounts/
│
├── recipes/                    # Recipe management
│   ├── urls.py                 # routes
│   ├── views.py
│   ├── serializers.py
│   ├── models.py
│   └── templates/recipes/
│
├── yumbook_backend/            # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── media/                      # Uploaded images
└── manage.py
---

## 🧑‍🍳 Core Models

### `CustomUser`
Extends Django’s `AbstractUser` with:
- `email` (unique)
- `bio`
- `profile_photo`

### `Recipe`
Fields include:
- `author` (FK to `CustomUser`)
- `title`
- `instructions`
- `prep_time`, `cook_time` (with duration validation)
- `images`
- `category`
- `servings`

### `IngredientsQuantity`
- Linked to `Recipe`
- Has `item` and `quantity` fields

---

## 🔐 Authentication

- **HTML Login:** `/accounts/login/`
- **API Token Login:** `POST /accounts/api/login/`
- **API Token Logout:** `POST /accounts/api/logout/`
- **Register (HTML):** `/accounts/register/`
- **Register (API):** `POST /accounts/api/register/`

Use the returned token to access authenticated endpoints:
Authorization: Token your_token_here


---

## 🧪 Testing the API

### 🔹 1. Register a user
`POST /accounts/api/register/`
```json
{
  "username": "chefamy",
  "email": "amy@example.com",
  "password": "strongpassword123"
}

### 🔹 2. Log in to get a token
POST /accounts/api/login/

json

{
  "username": "chefamy",
  "password": "strongpassword123"
}
Response:

json

{
  "token": "abcdef123456...",
  "user": {
    "id": 1,
    "username": "chefamy",
    "email": "amy@example.com"
  }
}

### 🔹 3. Create a recipe
POST /recipes/api/recipes/
(Include token in Authorization header)

json

{
  "title": "Lasagna",
  "instructions": "Layer pasta, meat sauce, and cheese. Bake for 45 minutes.",
  "prep_time": "00:30:00",
  "cook_time": "01:00:00",
  "category": "Italian",
  "servings": 4
}

### 🔹 4. Get your recipes
GET /recipes/api/recipes/

⚙️ Installation & Setup
Clone the repository:

bash
Copy code
git clone https://github.com/fredamakarie/yumbook-django.git
cd yumbook-django
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
Set up your .env file:

env
Copy code
DB_NAME=yumbook_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Access the app:

HTML interface → http://127.0.0.1:8000/

Admin dashboard → http://127.0.0.1:8000/admin/

API endpoints → http://127.0.0.1:8000/recipes/api/

## 🧠 Developer Notes
DRF Pagination is enabled (PAGE_SIZE = 6).

Recipes are user-scoped — users can only view, edit, or delete their own recipes.

Time fields (prep_time, cook_time) include robust validation to handle common mistakes like "30" or "00:45:00".

After logout, tokens are invalidated and cannot be reused.

## 🧠 Future Improvements

Public sharing of recipes

User following / favorites

API pagination and filtering

React or Vue frontend integration

🧾 License
This project is licensed under the MIT License.