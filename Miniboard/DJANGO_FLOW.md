# 🎓 Django Flow Explanation - Mini Noticeboard

## The Django MVT (Model-View-Template) Flow

### 1. **URL Request** → User visits a URL

```
User visits: http://localhost:8000/notice/1/
```

### 2. **URL Routing** → Match URL in `urls.py`

```python
# miniboard_project/urls.py
path('', include('notices.urls')),

# notices/urls.py
path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
```
✅ Matches! Calls `views.notice_detail(request, pk=1)`

### 3. **View Processing** → Execute view function

```python
# notices/views.py
def notice_detail(request, pk):
    notice = Notice.objects.get(pk=pk)  # Query database
    return render(request, 'notices/notice_detail.html', {'notice': notice})
```
- Gets the notice from database (Model)
- Prepares data for template

### 4. **Template Rendering** → Render HTML

```django
# templates/notices/notice_detail.html
<h1>{{ notice.title }}</h1>
<p>{{ notice.content }}</p>
<p>By: {{ notice.author }}</p>
```
- Django template engine replaces `{{ notice.title }}` with actual data
- Returns HTML to browser

### 5. **Response** → Browser displays page

```
Browser receives HTML and displays the page
```

---

## The Model Layer

### Defining Models
```python
# notices/models.py
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

### QuerySet Operations
```python
# Get all notices
all_notices = Notice.objects.all()

# Filter notices
pinned = Notice.objects.filter(is_pinned=True)

# Get one notice
notice = Notice.objects.get(pk=1)

# Create new
Notice.objects.create(title="New", content="...")

# Update
notice.title = "Updated"
notice.save()

# Delete
notice.delete()
```

---

## The View Layer

### Function-Based Views (FBV)

#### Simple View (Display Data)
```python
def home(request):
    notices = Notice.objects.all()
    return render(request, 'notices/home.html', {'notices': notices})
```

#### Form Handling View
```python
def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save()
            return redirect('notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    return render(request, 'notices/create_notice.html', {'form': form})
```

#### Detailed Flow:
1. **First visit (GET)**: Display empty form
2. **User fills & submits**: POST request
3. **Validate data**: Check if form is valid
4. **Save to DB**: If valid, create notice
5. **Redirect**: Send user to notice detail page

---

## The Template Layer

### Template Tags & Filters
```django
<!-- Variables -->
{{ notice.title }}

<!-- Loops -->
{% for notice in notices %}
    <h3>{{ notice.title }}</h3>
{% endfor %}

<!-- Conditions -->
{% if notice.is_pinned %}
    <span class="badge">Pinned</span>
{% endif %}

<!-- Filters -->
{{ notice.created_at|date:"F d, Y" }}
{{ notice.content|truncatewords:30 }}

<!-- URL Reversal -->
<a href="{% url 'notice_detail' notice.id %}">View</a>
```

---

## Complete Request Example

### Scenario: Edit a Notice

1. **User Action**
   - Clicks "Edit" on notice with id=5

2. **URL Routing**
   ```
   URL: /notice/5/edit/
   Matches: path('notice/<int:pk>/edit/', views.edit_notice, name='edit_notice')
   Calls: edit_notice(request, pk=5)
   ```

3. **View Processing**
   ```python
   def edit_notice(request, pk):
       notice = Notice.objects.get(pk=pk)  # Get from DB
       
       if request.method == 'POST':  # Form submitted
           form = NoticeForm(request.POST, instance=notice)
           if form.is_valid():
               form.save()  # Update DB
               return redirect('notice_detail', pk=notice.pk)
       else:  # First visit
           form = NoticeForm(instance=notice)  # Pre-fill form
       
       return render(request, 'notices/edit_notice.html', 
                    {'form': form, 'notice': notice})
   ```

4. **Template Rendering**
   ```django
   <form method="post">
       {% csrf_token %}
       {{ form.title }}
       {{ form.content }}
       <button type="submit">Save</button>
   </form>
   ```

5. **Browser Response**
   - First visit: Form displays with current data
   - After submission: Redirected to notice detail page

---

## Database Workflow

```
Model Definition
    ↓
makemigrations (Create migration file)
    ↓
migrate (Apply to database)
    ↓
QuerySet Operations (CRUD)
    ↓
Admin Interface (Manage data)
```

### Commands:
```bash
python manage.py makemigrations   # Detect model changes
python manage.py migrate           # Apply changes to DB
python manage.py shell             # Interactive Python shell
python manage.py createsuperuser   # Create admin user
```

---

## Common Patterns

### Pattern 1: List View
```python
def list_view(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
```

### Pattern 2: Detail View
```python
def detail_view(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'detail.html', {'item': item})
```

### Pattern 3: Create View
```python
def create_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'create.html', {'form': form})
```

### Pattern 4: Update View
```python
def update_view(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'update.html', {'form': form})
```

### Pattern 5: Delete View
```python
def delete_view(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list')
    return render(request, 'delete.html', {'item': item})
```

---

## Key Takeaways

✅ **URL** → Determines which view to call
✅ **View** → Processes request, queries database, prepares data
✅ **Model** → Defines database structure and ORM queries
✅ **Template** → Renders HTML with dynamic data
✅ **Context** → Dictionary passed from view to template
✅ **QuerySet** → Lazy, chainable database operations

This flow repeats for every request in Django!
