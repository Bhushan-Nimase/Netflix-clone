# 🎬 Netflix Clone (Django)

A full-stack **Netflix Clone** built using the **Django** framework. Users can browse, view details of movies, and explore content categorized by genres.

## 🚀 Features

- User authentication (login, logout, registration)
- Movie listing with categories (genres)
- Dynamic home page with carousel/banner
- Admin panel for managing content
- Movie detail page with information
- Responsive frontend using HTML, CSS, Bootstrap

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3
- Bootstrap 4
- Django Templates

**Backend:**
- Python 3.x
- Django 3.x or above

**Database:**
- SQLite (default)
- Can be configured to MySQL/PostgreSQL

---

## 📂 Project Structure

```

netflix-clone/
├── django\_netflix/         # Main Django project
│   ├── settings.py         # Project settings
│   └── urls.py             # Root URLs
├── stream/                 # App for movie streaming
│   ├── models.py           # Models (Category, Movie)
│   ├── views.py            # Views (home, movie\_detail)
│   ├── urls.py             # App URLs
│   ├── templates/          # HTML Templates
│   └── static/             # CSS/JS/Images
├── db.sqlite3              # Default database
└── manage.py               # Django CLI

````

---

## 🧑‍💻 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/netflix-clone-django.git
cd netflix-clone-django
````

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, use:

```bash
pip install django
```

---

## ⚙️ Run the Server

```bash
python manage.py migrate
python manage.py createsuperuser  # For admin access
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site.

---

## 🧠 Models Overview

### `Category` Model

* `name`: Genre name (e.g., Action, Comedy)

### `Movies` Model

* `title`, `description`, `image`, `category`

---

## 🛡️ Admin Panel

Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
Login with superuser credentials to manage movies and categories.

---

## ✍️ Author

**Bhushan Ashok Nimase**
[GitHub](https://github.com/Bhushan-Nimase)
[LinkedIn](https://linkedin.com/in/nimasebhushan20)


---

```

Let me know if your project has features like **watchlist**, **video player**, or **user profiles**, and I’ll update the README accordingly.
```
