# 📝 Quick Reference Commands

## Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (CMD)
venv\Scripts\activate.bat

# Deactivate
deactivate
```

## Package Management

```powershell
# Install all requirements
pip install -r requirements.txt

# Install single package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# List installed packages
pip list

# Check for outdated packages
pip list --outdated

# Upgrade pip
python -m pip install --upgrade pip
```

## Django Management Commands

### Database

```powershell
# Create migrations
python manage.py makemigrations

# Create migrations for specific app
python manage.py makemigrations tasks

# Show migrations
python manage.py showmigrations

# Apply migrations
python manage.py migrate

# Apply specific migration
python manage.py migrate tasks 0001

# Rollback migration
python manage.py migrate tasks 0001

# SQL for migration
python manage.py sqlmigrate tasks 0001
```

### Server

```powershell
# Run development server
python manage.py runserver

# Run on different port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### User Management

```powershell
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username
```

### Static Files

```powershell
# Collect static files
python manage.py collectstatic

# Collect without prompts
python manage.py collectstatic --noinput

# Clear collected static files
python manage.py collectstatic --clear
```

### Shell

```powershell
# Django shell
python manage.py shell

# Shell Plus (if installed)
python manage.py shell_plus
```

### Database Shell

```powershell
# Database shell
python manage.py dbshell
```

### Flush Database

```powershell
# Remove all data from database
python manage.py flush
```

## Testing

```powershell
# Run Django tests
python manage.py test

# Run Django tests for specific app
python manage.py test tasks

# Run with coverage
coverage run --source='.' manage.py test

# Run pytest
pytest

# Run pytest with verbose
pytest -v

# Run specific test file
pytest tasks/tests.py

# Run specific test class
pytest tasks/tests.py::TaskModelTest

# Run specific test method
pytest tasks/tests.py::TaskModelTest::test_task_creation

# Run with coverage
coverage run -m pytest
coverage report
coverage html

# Run tests and show print statements
pytest -s
```

## Git Commands

```bash
# Initialize repository
git init

# Check status
git status

# Add all files
git add .

# Add specific file
git add filename

# Commit changes
git commit -m "Your message"

# Push to remote
git push origin main

# Pull from remote
git pull origin main

# Create new branch
git checkout -b feature-name

# Switch branch
git checkout branch-name

# Merge branch
git merge branch-name

# View branches
git branch

# Delete branch
git branch -d branch-name

# View commit history
git log

# View remote repositories
git remote -v
```

## Docker Commands

```powershell
# Build and start containers
docker-compose up

# Build and start in background
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs

# Follow logs
docker-compose logs -f

# Execute command in container
docker-compose exec web python manage.py migrate

# Build containers
docker-compose build

# Rebuild containers
docker-compose up --build

# Remove volumes
docker-compose down -v

# List running containers
docker ps

# List all containers
docker ps -a
```

## Database Operations

### Backup Database (SQLite)

```powershell
# Copy database file
copy db.sqlite3 db_backup.sqlite3

# With timestamp
copy db.sqlite3 db_backup_$(Get-Date -Format 'yyyy-MM-dd').sqlite3
```

### Restore Database (SQLite)

```powershell
# Restore from backup
copy db_backup.sqlite3 db.sqlite3
```

### Export Data

```powershell
# Export all data
python manage.py dumpdata > data.json

# Export specific app
python manage.py dumpdata tasks > tasks_data.json

# Export with indentation
python manage.py dumpdata --indent 2 > data.json

# Export excluding auth
python manage.py dumpdata --exclude auth.permission > data.json
```

### Import Data

```powershell
# Import data
python manage.py loaddata data.json

# Import specific file
python manage.py loaddata tasks_data.json
```

## Debugging

```powershell
# Check for problems
python manage.py check

# Check deployment settings
python manage.py check --deploy

# Show project settings
python manage.py diffsettings

# Show URLs
python manage.py show_urls  # requires django-extensions
```

## Maintenance

```powershell
# Clean pyc files
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item

# Clean __pycache__ directories
Get-ChildItem -Recurse -Filter "__pycache__" -Directory | Remove-Item -Recurse

# Clean database
del db.sqlite3

# Clean migrations (keep __init__.py)
Get-ChildItem tasks\migrations -Exclude "__init__.py" | Remove-Item

# Clean collected static files
Remove-Item -Recurse -Force staticfiles\*
```

## Performance

```powershell
# Check for missing migrations
python manage.py makemigrations --check --dry-run

# Optimize database
python manage.py sqlsequencereset tasks

# Show slow queries (requires debug toolbar)
# Enable DEBUG_TOOLBAR in settings.py
```

## Security

```powershell
# Check for security issues
pip install safety
safety check

# Check for outdated packages
pip list --outdated

# Update all packages
pip list --outdated --format=freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```

## Useful Python Commands

```powershell
# Check Python version
python --version

# Check pip version
pip --version

# Show installed package info
pip show django

# Create requirements from environment
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Upgrade package
pip install --upgrade package-name
```

## Environment Variables

```powershell
# View environment variable
echo $env:DJANGO_SETTINGS_MODULE

# Set environment variable
$env:DJANGO_SETTINGS_MODULE="todo_project.settings"

# Set permanently (PowerShell profile)
# Edit: notepad $PROFILE
# Add: $env:DJANGO_SETTINGS_MODULE="todo_project.settings"
```

## Quick Development Workflow

```powershell
# 1. Activate environment
.\venv\Scripts\Activate.ps1

# 2. Create migrations
python manage.py makemigrations

# 3. Apply migrations
python manage.py migrate

# 4. Run tests
pytest

# 5. Run server
python manage.py runserver
```

## Quick Production Checklist

```powershell
# 1. Set DEBUG=False in .env
# 2. Update SECRET_KEY
# 3. Update ALLOWED_HOSTS
# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run with gunicorn
gunicorn todo_project.wsgi:application
```

## Troubleshooting Commands

```powershell
# Check Django installation
python -c "import django; print(django.get_version())"

# Check database connection
python manage.py dbshell

# Validate models
python manage.py validate  # Django < 1.9
python manage.py check

# Show project structure
tree /F

# Check port availability
netstat -an | findstr :8000

# Kill process on port 8000 (if needed)
# Find PID: netstat -ano | findstr :8000
# Kill: taskkill /PID <PID> /F
```

## VS Code Integration

### Tasks (tasks.json)

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Django Server",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python",
            "args": ["manage.py", "runserver"],
            "problemMatcher": []
        }
    ]
}
```

### Launch (launch.json)

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true
        }
    ]
}
```

## Aliases (Optional)

Add to PowerShell profile (`notepad $PROFILE`):

```powershell
# Django aliases
function djrun { python manage.py runserver }
function djmig { python manage.py makemigrations; python manage.py migrate }
function djtest { pytest }
function djshell { python manage.py shell }
function djsuper { python manage.py createsuperuser }
function djstatic { python manage.py collectstatic --noinput }
function djcheck { python manage.py check }

# Virtual environment
function vact { .\venv\Scripts\Activate.ps1 }
```

## Common Issues & Solutions

### Port 8000 already in use

```powershell
# Find process
netstat -ano | findstr :8000

# Kill process
taskkill /PID <PID> /F

# Or use different port
python manage.py runserver 8080
```

### Migration conflicts

```powershell
# Reset migrations
Remove-Item tasks\migrations\0*.py
python manage.py makemigrations
python manage.py migrate
```

### Static files not loading

```powershell
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT in settings.py
# Check STATIC_URL in settings.py
```

### Import errors

```powershell
# Reinstall requirements
pip install -r requirements.txt --force-reinstall

# Verify installation
pip list
```

---

**Pro Tip:** Bookmark this file for quick reference during development! 📌
