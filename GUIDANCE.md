# 📘 Complete Setup & Running Guide

This guide provides detailed step-by-step instructions for setting up and running the Library Management System project.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Initial Setup](#initial-setup)
4. [Running the Project](#running-the-project)
5. [Creating Sample Data](#creating-sample-data)
6. [User Roles & Permissions](#user-roles--permissions)
7. [Common Operations](#common-operations)
8. [Troubleshooting](#troubleshooting)
9. [Production Deployment](#production-deployment)

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version` or `python3 --version`

2. **pip (Python Package Manager)**
   - Usually comes with Python
   - Verify: `pip --version` or `pip3 --version`

3. **Git (Optional, for cloning)**
   - Download from: https://git-scm.com/downloads

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: At least 100MB free space
- **Internet Connection**: Required for installing packages

---

## 📦 Installation Steps

### Step 1: Get the Project

**Option A: Clone from GitHub**
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

**Option B: Download ZIP**
- Download the project ZIP file
- Extract it to your desired location
- Open terminal/command prompt in the extracted folder

### Step 2: Create Virtual Environment (Highly Recommended)

Creating a virtual environment isolates project dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify activation:**
- You should see `(venv)` at the beginning of your command prompt

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2.7
- Pillow 10.1.0 (for image handling)

**Expected output:**
```
Successfully installed Django-4.2.7 Pillow-10.1.0 ...
```

---

## ⚙️ Initial Setup

### Step 1: Create Database

Django uses migrations to create database tables.

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to create database
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, library, sessions
Running migrations:
  Applying library.0001_initial... OK
  Applying library.0002_book_content_file... OK
  ...
```

### Step 2: Create Admin User

Create a superuser account to access the admin panel and perform admin operations.

```bash
python manage.py createsuperuser
```

**Follow the prompts:**
```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

**Important Notes:**
- Username and email can be anything
- Password should be strong (at least 8 characters)
- Password won't show while typing (this is normal)

### Step 3: Create Media Directories (Optional)

The system will create these automatically, but you can create them manually:

```bash
# Windows
mkdir media
mkdir media\book_covers
mkdir media\book_content

# Linux/macOS
mkdir -p media/book_covers
mkdir -p media/book_content
```

---

## 🚀 Running the Project

### Start the Development Server

```bash
python manage.py runserver
```

**Expected output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 14, 2025 - 00:00:00
Django version 4.2.7, using settings 'library_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Access the Application

1. **Main Website**: Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

2. **Admin Panel**: Go to:
   ```
   http://127.0.0.1:8000/admin/
   ```
   Login with the superuser credentials you created.

### Stop the Server

Press `CTRL + C` (or `CTRL + BREAK` on Windows) in the terminal to stop the server.

---

## 📚 Creating Sample Data

### Method 1: Using Admin Panel (Recommended)

1. **Login to Admin Panel**
   - Go to http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

2. **Add Authors**
   - Click on "Authors"
   - Click "Add Author"
   - Fill in: Name, Birth Date (optional), Biography (optional)
   - Click "Save"

3. **Add Genres**
   - Click on "Genres"
   - Click "Add Genre"
   - Fill in: Name, Description (optional)
   - Click "Save"

4. **Add Books**
   - Click on "Books"
   - Click "Add Book"
   - Fill in all required fields:
     - Title
     - Author (select from dropdown)
     - Genre (optional)
     - ISBN (optional)
     - Description (optional)
     - Published Date (optional)
     - Total Copies
     - Available Copies
     - Cover Image (optional, upload a JPG/PNG)
     - Content File (optional, upload PDF/DOC/etc.)
   - Click "Save"

### Method 2: Using Web Interface

1. **Login as Admin**
   - Go to http://127.0.0.1:8000/
   - Click "Login"
   - Use your admin credentials

2. **Add Content**
   - Click "Add New Book" (visible only to admins)
   - Fill in the form and save
   - Repeat for authors and genres

### Sample Data Suggestions

**Authors:**
- J.K. Rowling (Born: 1965-07-31)
- George R.R. Martin (Born: 1948-09-20)
- Stephen King (Born: 1947-09-21)

**Genres:**
- Fiction
- Non-Fiction
- Science Fiction
- Mystery
- Romance

**Books:**
- Add 5-10 books with different genres
- Upload cover images for visual appeal
- Upload content files (PDFs) for testing content access

---

## 👥 User Roles & Permissions

### Admin Users

**Capabilities:**
- ✅ Create, edit, delete books
- ✅ Create authors and genres
- ✅ View all borrowings
- ✅ Access admin panel
- ✅ View/download all book content (without borrowing)
- ✅ Manage all aspects of the system

**How to Create Admin:**
```bash
python manage.py createsuperuser
```

**Or promote existing user:**
- Go to Admin Panel → Users
- Select a user
- Check "Staff status" and "Superuser status"
- Save

### Regular Users

**Capabilities:**
- ✅ Register and login
- ✅ Browse and search books
- ✅ View book details
- ✅ Borrow books
- ✅ View/download content of borrowed books only
- ✅ Return books
- ✅ View their own borrowing history
- ❌ Cannot add/edit/delete books
- ❌ Cannot add authors/genres
- ❌ Cannot access admin panel

**How Regular Users Work:**
1. Register at http://127.0.0.1:8000/register/
2. Login with credentials
3. Browse books and borrow
4. After borrowing, they can access book content

---

## 🔄 Common Operations

### For Admins

#### Adding a New Book
1. Login as admin
2. Go to "Books" → "Add New Book"
3. Fill in:
   - Title: "The Great Gatsby"
   - Author: Select from dropdown (or add new)
   - Genre: Select from dropdown (or add new)
   - Total Copies: 5
   - Available Copies: 5
   - Cover Image: Upload a book cover
   - Content File: Upload PDF/DOC file
4. Click "Save Book"

#### Managing Borrowings
1. Go to "Borrowings"
2. View all active and returned borrowings
3. Click "Return" to mark a book as returned

### For Regular Users

#### Registering
1. Go to http://127.0.0.1:8000/register/
2. Fill in:
   - Username
   - First Name (optional)
   - Last Name (optional)
   - Email
   - Password
   - Confirm Password
3. Click "Register"
4. You'll be redirected to login

#### Borrowing a Book
1. Login to your account
2. Browse books or search for a specific book
3. Click "Borrow" on an available book
4. Fill in due date
5. Click "Borrow Book"
6. The book is now borrowed and you can access its content

#### Viewing/Downloading Content
1. Go to "My Borrowings"
2. Find a borrowed book
3. Click on the book title to go to detail page
4. Click "View Content" to read online
5. Click "Download" to download the file

#### Returning a Book
1. Go to "My Borrowings"
2. Find the book you want to return
3. Click "Return"
4. Confirm the return
5. Book availability updates automatically

---

## 🐛 Troubleshooting

### Issue 1: "No such table: library_book"

**Error Message:**
```
django.db.utils.OperationalError: no such table: library_book
```

**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue 2: Static Files Not Loading

**Symptom:** CSS styles not applied, page looks unstyled

**Solution:**
1. Ensure you're running server from project root
2. Check that `static/css/style.css` exists
3. Restart the server:
   ```bash
   python manage.py runserver
   ```

### Issue 3: Images Not Uploading

**Symptom:** Image upload fails or images don't display

**Solution:**
1. Check that `media/` directory exists
2. Ensure `media/book_covers/` directory exists
3. Check file permissions (should be writable)
4. Verify file size (should be reasonable, < 10MB)

### Issue 4: "ModuleNotFoundError"

**Error Message:**
```
ModuleNotFoundError: No module named 'django'
```

**Solution:**
1. Activate virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Issue 5: Port Already in Use

**Error Message:**
```
Error: That port is already in use.
```

**Solution:**
1. Use a different port:
   ```bash
   python manage.py runserver 8001
   ```
2. Or find and stop the process using port 8000

### Issue 6: Cannot Access Content After Borrowing

**Symptom:** User borrowed book but can't view/download content

**Solution:**
1. Verify the book has a content file uploaded
2. Check that borrowing email matches user email
3. Ensure borrowing is not marked as returned
4. Check browser console for errors

### Issue 7: Database Locked

**Error Message:**
```
database is locked
```

**Solution:**
1. Close any other programs accessing the database
2. Restart the Django server
3. If persistent, delete `db.sqlite3` and run migrations again

---

## 🚀 Production Deployment

### Important Security Changes

Before deploying to production:

1. **Change SECRET_KEY**
   - Edit `library_project/settings.py`
   - Generate a new secret key
   - Never commit it to version control

2. **Set DEBUG = False**
   ```python
   DEBUG = False
   ```

3. **Configure ALLOWED_HOSTS**
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Use Production Database**
   - Consider PostgreSQL or MySQL instead of SQLite
   - Update DATABASES in settings.py

5. **Configure Static Files**
   - Use `python manage.py collectstatic`
   - Configure web server (Nginx/Apache) to serve static files

6. **Use HTTPS**
   - Configure SSL certificate
   - Redirect HTTP to HTTPS

7. **Set Up Environment Variables**
   - Use environment variables for sensitive data
   - Never hardcode secrets

### Deployment Platforms

- **Heroku**: Easy Django deployment
- **AWS**: Scalable cloud hosting
- **DigitalOcean**: Simple VPS hosting
- **PythonAnywhere**: Free Django hosting

---

## 📝 Additional Notes

### File Structure
- **Database**: `db.sqlite3` (created automatically)
- **Media Files**: Stored in `media/` directory
- **Static Files**: Stored in `static/` directory

### Backup Recommendations
- Regularly backup `db.sqlite3`
- Backup `media/` directory
- Keep migration files in version control

### Performance Tips
- Use pagination for large datasets (already implemented)
- Optimize images before upload
- Consider caching for production

---

## ✅ Quick Checklist

Before running the project, ensure:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Migrations run (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)
- [ ] Server running (`python manage.py runserver`)
- [ ] Can access http://127.0.0.1:8000/

---

## 🆘 Getting Help

If you encounter issues:

1. Check this guide's troubleshooting section
2. Review Django documentation: https://docs.djangoproject.com/
3. Check error messages in terminal
4. Verify all steps were followed correctly
5. Open an issue on GitHub

---

**Happy Coding! 🎉**

For more information, see [README.md](README.md)

