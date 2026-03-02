# 📋 Mini Noticeboard

A lightweight Django web application for posting and managing campus notices and announcements. Perfect for learning Django's core concepts: URL routing, views, templates, and models.

## 🎯 Features

- **Post Notices**: Create short notices with title, content, and author information
- **Pin Important Notices**: Mark urgent notices to keep them at the top
- **Edit & Delete**: Update or remove notices anytime
- **Timestamps**: Automatic tracking of creation and update times
- **Clean UI**: Beautiful Bootstrap-based interface
- **Admin Panel**: Django admin for advanced management
- **Responsive Design**: Works seamlessly on all devices

## 🚀 Project Structure

```
Miniboard/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── db.sqlite3                         # Database (auto-created)
│
├── miniboard_project/                 # Project configuration
│   ├── __init__.py
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Project URL routing
│   └── wsgi.py                        # WSGI configuration
│
├── notices/                           # Main app
│   ├── __init__.py
│   ├── models.py                      # Notice model definition
│   ├── views.py                       # View functions (logic)
│   ├── forms.py                       # Notice form
│   ├── admin.py                       # Admin configuration
│   ├── apps.py                        # App configuration
│   ├── urls.py                        # App URL routing
│   ├── tests.py                       # Unit tests
│   └── migrations/                    # Database migrations
│
└── templates/                         # HTML templates
    ├── base.html                      # Base template (navbar, footer)
    └── notices/
        ├── home.html                  # Homepage with notice list
        ├── notice_detail.html         # Single notice view
        ├── create_notice.html         # Create new notice
        ├── edit_notice.html           # Edit existing notice
        ├── delete_confirm.html        # Delete confirmation
        └── about.html                 # About page (static)
```

## 🛠️ Installation

### 1. Clone the Repository
```bash
cd Miniboard
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create and Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (for Admin Access)
```bash
python manage.py createsuperuser
# Follow the prompts to create admin credentials
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## 📖 Usage

### Via Web Interface
1. **Home Page**: View all posted notices
2. **Create Notice**: Click "New Notice" and fill in the form
3. **View Details**: Click "View" on any notice
4. **Edit Notice**: Edit your notice content
5. **Delete Notice**: Remove notices you no longer need
6. **About Page**: Learn more about the app

### Via Admin Panel
1. Navigate to `http://localhost:8000/admin/`
2. Log in with your superuser credentials
3. Manage notices with advanced filtering and search options

## 🔑 Key Django Concepts Covered

### 1. **URL Routing** (`notices/urls.py`)
Maps URL patterns to view functions:
```python
path('', views.home, name='home'),
path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
```

### 2. **Views** (`notices/views.py`)
Functions that handle requests and return responses:
```python
def home(request):
    notices = Notice.objects.all()
    return render(request, 'notices/home.html', {'notices': notices})
```

### 3. **Models** (`notices/models.py`)
Database table definitions:
```python
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 4. **Templates** (`templates/notices/`)
HTML files rendered with context data:
```django
{% for notice in notices %}
    <h3>{{ notice.title }}</h3>
    <p>by {{ notice.author }}</p>
{% endfor %}
```

### 5. **Forms** (`notices/forms.py`)
ModelForm for handling user input:
```python
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'author', 'is_pinned']
```

## 📊 Database Schema

### Notice Model
| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key (auto-generated) |
| title | CharField(200) | Notice title |
| content | TextField | Notice content |
| author | CharField(100) | Author name |
| created_at | DateTimeField | Creation timestamp (auto) |
| updated_at | DateTimeField | Last update timestamp (auto) |
| is_pinned | BooleanField | Pin status |

## 🧪 Testing

Run the test suite:
```bash
python manage.py test notices
```

## 📝 Common Tasks

### Add Sample Data
```bash
python manage.py shell
```
```python
from notices.models import Notice
Notice.objects.create(
    title="Welcome",
    content="Welcome to Mini Noticeboard!",
    author="Admin"
)
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Reset Database
```bash
# Delete db.sqlite3
# Then run migrations again
python manage.py makemigrations
python manage.py migrate
```

## 🎓 Learning Resources

**Django Concepts Used:**
- Models (ORM)
- Views & URL Routing
- Templates & Template Tags
- Forms & Validation
- Admin Interface
- Migrations
- QuerySets

**Next Steps to Extend:**
- Add user authentication
- Implement comments on notices
- Add categories/tags
- Create API endpoints (Django REST Framework)
- Add search functionality
- Implement pagination
- Deploy to production (Heroku, AWS, etc.)

## ⚙️ Configuration

Key settings in `miniboard_project/settings.py`:
- `DEBUG = True` (set to False in production)
- `ALLOWED_HOSTS = ['*']` (specify domains in production)
- `DATABASES` - Configure database
- `INSTALLED_APPS` - List of installed applications
- `TEMPLATES` - Template configuration

## 🔐 Security Notes

⚠️ **Development Only:**
- This app is configured for development
- Never use `SECRET_KEY` from this project in production
- Always set `DEBUG = False` in production
- Add allowed hosts to `ALLOWED_HOSTS`
- Use environment variables for sensitive data

## 📄 License

This project is for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and improve this project for learning purposes.

## 💡 Tips

1. **Explore the Admin Panel**: It's a great way to understand models
2. **Read the Code**: Comments explain key concepts
3. **Experiment**: Try modifying models, views, and templates
4. **Debug**: Use `print()` statements and Django debug toolbar
5. **Check Console**: View SQL queries and errors

---

**Made for learning Django** 🎓
