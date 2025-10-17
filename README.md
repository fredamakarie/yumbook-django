YumBook — Recipe Management Web App

YumBook is a full-stack Django recipe management application where users can create, edit, delete, and browse recipes.
It includes both HTML pages (frontend templates) and REST API endpoints powered by Django REST Framework (DRF).

Users can:

Store and manage personal recipes

Add ingredients with quantities

Upload images

Browse all recipes

Search by ingredients or category

Use the REST API for integration with frontend apps or mobile clients

🚀 Features
👩‍🍳 Core Functionality

Create, read, update, and delete recipes

Manage ingredients and their quantities

View detailed recipe pages

Upload recipe images

🔐 Authentication

User registration and login (HTML and API)

DRF token authentication

Restricted access to editing/deleting recipes (only the author)

🧭 API + HTML Separation

/recipes/ → HTML-based pages for web users

/api/recipes/ → REST API endpoints for external clients

🔎 Search

Filter and search recipes by ingredients or category

🏗️ Tech Stack
Layer	Technology
Backend Framework	Django 5.x
API Framework	Django REST Framework
Authentication	DRF Token Auth
Database	postgreSQL
Frontend	Django Templates (HTML, CSS, JS)
Media Storage	Django File Storage (images in /media/)
🧩 Project Structure
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

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/yumbook.git
cd yumbook

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # macOS / Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver


Visit:

Admin Panel: http://127.0.0.1:8000/admin/

HTML Recipes App: http://127.0.0.1:8000/recipes/

API Endpoints: http://127.0.0.1:8000/api/recipes/

🔑 API Endpoints Overview
Endpoint	Method	Description
/api/recipes/	GET	List all recipes
/api/recipes/<id>/	GET	Retrieve a specific recipe
/api/recipes/	POST	Create a new recipe
/api/recipes/<id>/	PUT/PATCH	Update a recipe
/api/recipes/<id>/	DELETE	Delete a recipe
/api/accounts/register/	POST	Register a new user
/api/accounts/login/	POST	Obtain authentication token
🧾 Example Recipe JSON
{
  "id": 1,
  "title": "Spaghetti Bolognese",
  "category": "Dinner",
  "ingredients": [
    {"item": "Spaghetti", "quantity": "200g"},
    {"item": "Ground Beef", "quantity": "150g"},
    {"item": "Tomato Sauce", "quantity": "1 cup"}
  ],
  "instructions": "Boil spaghetti. Cook beef. Mix with sauce.",
  "cook_time": "00:30:00",
  "prep_time": "00:15:00",
  "author": "admin"
}

🖼️ Screenshots

(Optional — add later)
Add screenshots of your recipe list, detail, and admin pages here.

🧪 Testing

Run Django’s test suite:

python manage.py test

🧰 Development Notes

Static and media files are served locally in debug mode.

To serve media in production, configure a storage backend (e.g., S3, Cloudinary).

Templates use Bootstrap / custom CSS (optional).

🤝 Contributing

Fork the project

Create a new feature branch (git checkout -b feature/new-feature)

Commit your changes (git commit -m "Add new feature")

Push to your branch (git push origin feature/new-feature)

Open a Pull Request

🧠 Future Improvements

Public sharing of recipes

User following / favorites

API pagination and filtering

React or Vue frontend integration

🪪 License

This project is licensed under the MIT License — see the LICENSE file for details