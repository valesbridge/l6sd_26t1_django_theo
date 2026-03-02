# 🚀 Quick Start Guide - Mini Noticeboard

## Step 1: Setup Environment
```bash
# Activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

## Step 2: Install Django
```bash
pip install -r requirements.txt
```

## Step 3: Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 4: Create Admin User
```bash
python manage.py createsuperuser
# Enter username, email, password
```

## Step 5: Run Server
```bash
python manage.py runserver
```

## Step 6: Access the App
- **Main App**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

## 📍 URL Routes

| URL | Purpose |
|-----|---------|
| `/` | Home - List all notices |
| `/create/` | Create a new notice |
| `/notice/<id>/` | View notice details |
| `/notice/<id>/edit/` | Edit a notice |
| `/notice/<id>/delete/` | Delete a notice |
| `/about/` | About page |
| `/admin/` | Django admin panel |

## 🎯 Core Files to Understand

1. **models.py** - Define Notice model
2. **views.py** - Handle requests and render templates
3. **urls.py** - Route URLs to views
4. **forms.py** - Create form for notices
5. **admin.py** - Configure admin interface
6. **templates/** - HTML files with Django template tags

## 💾 First Notice

Via web:
1. Click "+ New Notice"
2. Fill in title, content, author
3. Click "Create Notice"

Via admin:
1. Go to `/admin/`
2. Click "Notices" → "Add Notice"
3. Fill in details and save

## 🧪 Quick Test

```bash
python manage.py test notices
```

## 📚 Next Steps

- Add user authentication (Django auth)
- Add comments feature
- Create API with Django REST Framework
- Deploy to Heroku/AWS
- Add search and filters
