# Employee Management System

A web-based Employee Management System built using **Python and Django**. This project provides an organized platform to manage employee records, handle user authentication, and perform employee management operations through a user-friendly interface.

## 🚀 Project Overview

The Employee Management System is designed to simplify employee record management through a Django-based web application.

It demonstrates practical implementation of Django concepts such as Models, Views, Templates (MVT), ORM, Authentication, CRUD operations, and database integration.

## ✨ Features

- **User Authentication** – User registration, login, and logout.
- **Employee Management** – Add, view, update, and delete employee records.
- **Soft Delete** – Deleted employee records can be excluded from active listings without permanently removing them from the database.
- **Employee Details** – View individual employee information.
- **Database Integration** – Manage employee data using Django ORM.
- **Image Support** – Support for employee images and media files.
- **Responsive Interface** – Structured user interface using HTML, CSS, and Bootstrap-related components.
- **Form Validation** – Handle form input and validation.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling |
| JavaScript | Frontend interactions |
| Bootstrap 5 | UI components |
| Django Crispy Forms | Form rendering |
| Pillow | Image processing |

## 📂 Project Structure

```text
Django/
│
├── Employee_main/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── employees/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
├── media/
├── staticfiles/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MeeranHusain/Django.git
```

### 2. Navigate to the project directory

```bash
cd Django
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## 📋 Application Modules

### Accounts Module
- User registration
- User login
- User logout
- Authentication and session management

### Employees Module
- Employee listing
- Add employee records
- View employee details
- Update employee information
- Delete employee records
- Soft-delete handling

## 🧠 Django Concepts Implemented

- Django MVT Architecture
- URL Routing
- Function-Based Views
- Django Models and ORM
- Database Migrations
- Django Authentication
- Django Forms
- Django Messages Framework
- Template Inheritance and Template Tags
- Static and Media File Handling
- CRUD Operations

## 🔮 Future Enhancements

- Role-based access control
- Department management improvements
- Employee search and filtering
- Pagination
- Advanced dashboard and reporting
- Django REST Framework API integration
- Production deployment

## 👨‍💻 Developer

**Meeran Husain**

Software Developer | Python & Django Learner

- GitHub: [MeeranHusain](https://github.com/MeeranHusain)
- Repository: [Django – Employee Management System](https://github.com/MeeranHusain/Django)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python & Django.**
