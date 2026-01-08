# 📝 Advanced To-Do List Application

A modern, full-featured task management web application built with Django. Manage your tasks efficiently with a beautiful, responsive interface.

## ✨ Features

- 🔐 **User Authentication** - Secure registration and login system
- ✅ **Task Management** - Create, read, update, and delete tasks
- 🎯 **Priority Levels** - Set task priorities (Low, Medium, High)
- 📅 **Due Dates** - Track deadlines for your tasks
- 🔍 **Advanced Filtering** - Filter by status, priority, and due date
- 🔎 **Search Functionality** - Quickly find tasks
- 📱 **Responsive Design** - Works perfectly on all devices
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 👤 **User Profiles** - Manage your personal information
- 🛡️ **Admin Panel** - Comprehensive admin interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todo_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Create superuser
docker-compose exec web python manage.py createsuperuser

# View logs
docker-compose logs -f
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
coverage run -m pytest
coverage report
coverage html  # Generate HTML report
```

## 📁 Project Structure

- `todo_project/` - Project configuration
- `tasks/` - Main application
  - `models.py` - Database models
  - `views.py` - View logic
  - `forms.py` - Form definitions
  - `urls.py` - URL routing
  - `templates/` - HTML templates
  - `static/` - CSS, JavaScript, images

## 🛠️ Technologies Used

- **Backend**: Django 5.0, Python 3.x
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Styling**: Custom CSS with modern gradients and animations
- **Icons**: Lucide Icons (via CDN)

## 📝 Usage

1. **Register** a new account or **login** with existing credentials
2. **Create tasks** with titles, descriptions, priorities, and due dates
3. **Filter tasks** by status (All, Active, Completed) or priority
4. **Search** for specific tasks using the search bar
5. **Mark tasks** as completed when done
6. **Edit or delete** tasks as needed
7. **View your profile** and update your information

## 🔒 Security Features

- CSRF protection enabled
- Password hashing with Django's built-in system
- Session security
- XSS protection
- SQL injection prevention
- Secure authentication system

## 🎨 UI Features

- Modern gradient color scheme
- Smooth animations and transitions
- Responsive grid layout
- Interactive hover effects
- Toast notifications for actions
- Loading states
- Empty state illustrations

## 📈 Future Enhancements

- Task categories and tags
- Task sharing and collaboration
- Recurring tasks
- Task attachments
- Email notifications
- Mobile app (React Native/Flutter)
- Dark mode toggle
- Task statistics and analytics
- Calendar view
- Export/Import functionality

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed as a demonstration of full-stack Django development skills.

## 🙏 Acknowledgments

- Django Documentation
- Django Community
- Bootstrap/Modern CSS practices
- Open source community
