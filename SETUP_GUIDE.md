# 🚀 Complete Setup Guide - TaskMaster Django To-Do Application

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+** (Python 3.10 or 3.11 recommended)
- **pip** (Python package installer)
- **Git** (optional, for version control)
- **Virtual Environment** (recommended)

## 🔧 Step-by-Step Installation

### Step 1: Navigate to Project Directory

```powershell
cd "d:\Programming\Django project\AdvanceToDo"
```

### Step 2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3: Install Dependencies

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**Installed Packages:**
- Django 5.0.2
- python-decouple 3.8
- Pillow 10.2.0
- django-crispy-forms 2.1
- crispy-bootstrap4 2.0
- gunicorn 21.2.0
- whitenoise 6.6.0
- pytest 8.0.0
- pytest-django 4.8.0
- coverage 7.4.1

### Step 4: Configure Environment Variables

The `.env` file has already been created for you with development settings. For production, update these values:

```env
SECRET_KEY=your-production-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Step 5: Create Database Tables

```powershell
# Create migrations for tasks app
python manage.py makemigrations tasks

# Apply all migrations
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)

```powershell
python manage.py createsuperuser
```

Follow the prompts to create your admin account:
- Username: (your choice)
- Email: (your email)
- Password: (create a strong password)

### Step 7: Collect Static Files

```powershell
python manage.py collectstatic --noinput
```

This copies all static files (CSS, JavaScript) to the `staticfiles` directory.

### Step 8: Run Development Server

```powershell
python manage.py runserver
```

## 🌐 Access the Application

Once the server is running, you can access:

- **Main Application**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **About Page**: http://localhost:8000/about

## 👤 First-Time Usage

1. **Register a New Account**
   - Go to http://localhost:8000
   - Click "Sign Up" or "Get Started Free"
   - Fill in your details (first name, last name, username, email, password)
   - Click "Create Account"

2. **Login**
   - Click "Login" or "Sign In"
   - Enter your username and password
   - You'll be redirected to your task list

3. **Create Your First Task**
   - Click "Add Task" or "Create New Task"
   - Fill in:
     - Task Title (required)
     - Description (optional)
     - Priority (Low, Medium, High)
     - Status (Pending, In Progress, Completed)
     - Due Date (optional)
   - Click "Create Task"

4. **Manage Tasks**
   - **View**: Click on a task card to see full details
   - **Edit**: Click the edit icon (pencil) on any task
   - **Delete**: Click the delete icon (trash) on any task
   - **Mark Complete**: Click "Mark Complete" button on task
   - **Filter**: Use status filters (All, Active, Completed)
   - **Search**: Use the search box to find specific tasks
   - **Sort**: Sort by date, priority, or title

5. **Update Your Profile**
   - Click on your username in the navigation
   - Select "Profile"
   - Update your personal information
   - Upload a profile picture
   - View your task statistics

## 🔐 Admin Panel Features

Access the admin panel at http://localhost:8000/admin

**Features:**
- User management (create, edit, delete users)
- Task management (view all tasks, bulk actions)
- User profiles management
- Bulk actions (mark completed, set priority)
- Advanced filtering and search

## 🧪 Running Tests

```powershell
# Run all tests
pytest

# Run tests with coverage
coverage run -m pytest
coverage report

# Generate HTML coverage report
coverage html
# Open htmlcov/index.html in browser
```

## 🐳 Docker Deployment (Optional)

If you want to use Docker:

```powershell
# Build and run containers
docker-compose up -d

# Create superuser in container
docker-compose exec web python manage.py createsuperuser

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

## 📁 Project Structure

```
AdvanceToDo/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── .env.example             # Example environment file
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── pytest.ini               # Pytest configuration
├── todo_project/            # Project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── tasks/                   # Main application
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── urls.py              # App URL routing
│   ├── forms.py             # Form definitions
│   ├── tests.py             # Unit tests
│   ├── migrations/          # Database migrations
│   │   └── __init__.py
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── tasks/
│   │   │   ├── home.html
│   │   │   ├── task_list.html
│   │   │   ├── task_form.html
│   │   │   ├── task_detail.html
│   │   │   ├── task_confirm_delete.html
│   │   │   └── about.html
│   │   └── registration/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── profile.html
│   └── static/              # Static files
│       ├── css/
│       │   └── style.css    # Main stylesheet
│       ├── js/
│       │   └── main.js      # Main JavaScript
│       └── images/
├── media/                   # User uploaded files
│   └── avatars/            # Profile pictures
└── staticfiles/            # Collected static files
```

## 🛠️ Troubleshooting

### Issue: ModuleNotFoundError: No module named 'decouple'

**Solution:**
```powershell
pip install python-decouple
```

### Issue: ImportError: cannot import name 'url' from 'django.conf.urls'

**Solution:** This project uses Django 5.0 which uses `path()` instead of `url()`. Make sure you're using Django 5.0.2.

### Issue: Static files not loading

**Solution:**
```powershell
python manage.py collectstatic --noinput
```

### Issue: Database errors

**Solution:**
```powershell
# Delete database and migrations
del db.sqlite3
# Remove migration files (keep __init__.py)
python manage.py makemigrations
python manage.py migrate
```

### Issue: Permission denied when activating venv

**Solution (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🎨 Customization

### Change Color Scheme

Edit `tasks/static/css/style.css` and modify CSS variables:

```css
:root {
    --primary: #667eea;
    --secondary: #764ba2;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
}
```

### Add New Features

1. Create new models in `tasks/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Update admin in `tasks/admin.py`
5. Create views in `tasks/views.py`
6. Add URLs in `tasks/urls.py`
7. Create templates in `tasks/templates/`

## 📈 Performance Tips

1. **Enable Caching** (for production)
   - Add Redis or Memcached
   - Configure in `settings.py`

2. **Database Optimization**
   - Use PostgreSQL for production
   - Add database indexes
   - Use select_related() and prefetch_related()

3. **Static Files**
   - Use CDN for static files
   - Enable compression
   - Configure browser caching

## 🔒 Security Best Practices

1. **Never commit .env file** (already in .gitignore)
2. **Use strong SECRET_KEY** in production
3. **Set DEBUG=False** in production
4. **Use HTTPS** in production
5. **Regular security updates**: `pip list --outdated`
6. **Enable CSRF protection** (already enabled)
7. **Use secure passwords** for admin accounts

## 📝 Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make changes and test**
   ```powershell
   python manage.py test
   pytest
   ```

3. **Run linting** (optional)
   ```powershell
   pip install flake8
   flake8 .
   ```

4. **Commit changes**
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

5. **Push to repository**
   ```bash
   git push origin feature/new-feature
   ```

## 🚀 Production Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn todo_project.wsgi
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### AWS/DigitalOcean Deployment

1. Set up server (Ubuntu recommended)
2. Install Python, pip, PostgreSQL
3. Clone repository
4. Install dependencies
5. Configure Nginx and Gunicorn
6. Set up SSL certificate (Let's Encrypt)
7. Configure domain and DNS

## 📚 Additional Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Django Tutorial**: https://docs.djangoproject.com/en/5.0/intro/tutorial01/
- **Python Documentation**: https://docs.python.org/3/
- **Bootstrap Documentation**: https://getbootstrap.com/
- **Font Awesome Icons**: https://fontawesome.com/

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Support

For issues or questions:
- Check the troubleshooting section
- Review Django documentation
- Check existing GitHub issues
- Create a new issue with details

## ✅ Success Checklist

- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Database migrations applied
- [ ] Superuser created
- [ ] Static files collected
- [ ] Development server running
- [ ] Can access http://localhost:8000
- [ ] Can login to admin panel
- [ ] Can create and manage tasks
- [ ] Tests passing

## 🎉 Congratulations!

Your TaskMaster Django To-Do application is now fully set up and ready to use!

**Next Steps:**
1. Explore the application features
2. Create some test tasks
3. Customize the design
4. Add new features
5. Deploy to production

Happy Coding! 🚀
