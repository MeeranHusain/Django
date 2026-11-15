# Employee Management System

A web-based **Employee Management System** developed using **Python and Django** to manage employee records, user authentication, and employee information through a structured and user-friendly web interface.

This project demonstrates practical implementation of Django's MVT architecture, ORM, ModelForms, authentication, CRUD operations, and database integration.

## 🚀 Project Overview

The Employee Management System provides a centralized platform for maintaining employee information.

Users can register and log in to access the application, while employee records can be created, viewed, updated, and soft-deleted.

The project is being developed incrementally, with a focus on understanding Django fundamentals, writing maintainable code, and implementing practical backend development concepts.

## ✨ Features

### 🔐 User Authentication
- User registration.
- User login and logout.
- Django authentication system.
- Session-based authentication.
- Success and error notifications.

### 👨‍💼 Employee Management
- Add new employee records.
- View employee details.
- Update employee information.
- Soft-delete employee records.
- Display employee profile images.
- Manage employee active/inactive status.

### 🏢 Employee Information
- First name and last name.
- Email address.
- Designation.
- Salary.
- Joining date.
- Department.
- Reporting manager.
- Employee profile image.

### 🛡️ Form Validation & Security
- Django ModelForms.
- Server-side form validation.
- CSRF protection.
- Login-protected pages.
- Permission-based access checks being developed.

### 🎨 User Interface
- Structured and responsive interface.
- Custom CSS styling.
- Bootstrap 5 form integration.
- Font Awesome icons.
- Custom notification messages.
- Custom 404 error page.

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
| Git & GitHub | Version control |

## 📂 Project Structure

```text
Django/
│
├── Employee_main/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── static/
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
│   ├── forms.py
│   └── admin.py
│
├── templates/
│
├── media/
│
├── staticfiles/
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/MeeranHusain/Django.git
```

### 2. Navigate to the Project Directory

```bash
cd Django
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate Virtual Environment

**Windows CMD:**

```cmd
myenv\Scripts\activate.bat
```

**Windows PowerShell:**

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## 📋 Application Modules

### 1. Accounts

Responsible for user authentication and account management.

- Registration
- Login
- Logout
- Session management
- Authentication notifications

### 2. Employees

Responsible for employee record management.

- Employee listing
- Add employee
- Employee details
- Edit employee
- Soft delete
- Department and manager relationships
- Employee image handling

## 🧠 Django Concepts Implemented

This project provides hands-on experience with:

- Django MVT Architecture
- Django URL Routing
- Function-Based Views
- Django Models and ORM
- Database Migrations
- Django Authentication
- Django Forms and ModelForms
- Django Messages Framework
- Django Template Language
- Template Tags and Filters
- Static and Media File Handling
- CRUD Operations
- Soft Delete Implementation
- Django Permissions

## 🔮 Future Enhancements

- Complete Role-Based Access Control (RBAC).
- Admin, Staff Read Only, and Staff Editor roles.
- Department management improvements.
- Employee search and filtering.
- Pagination.
- Advanced dashboard and reporting.
- Django REST Framework integration.
- Production deployment.

## 📸 Screenshots

Screenshots of the application will be added here as the project interface evolves.

Suggested screenshots:

- Login Page
- Registration Page
- Employee Dashboard
- Add Employee Form
- Employee Details Page
- Edit Employee Form
- Django Admin Dashboard

## 👨‍💻 Developer

**Meeran Husain**

Software Developer | Python & Django Developer (Learning & Building)

Interested in backend development, database management, REST APIs, and building practical web applications.

- GitHub: [MeeranHusain](https://github.com/MeeranHusain)
- Project Repository: [Employee Management System](https://github.com/MeeranHusain/Django)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python & Django.**
