# Quick Setup Guide

## Step-by-Step Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User (Optional but Recommended)
```bash
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### 4. Run Server
```bash
python manage.py runserver
```

### 5. Access the Application
- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Quick Demo Data Setup

After running migrations, you can add sample data through:
1. Admin panel (http://127.0.0.1:8000/admin/)
2. Or use the web interface to add books, authors, and genres

## For Your Presentation Tomorrow

### What to Show:
1. **Home Page** - Statistics dashboard
2. **Add a Book** - Show the form with all fields
3. **Search Functionality** - Search by title/author
4. **Book Details** - Show book information
5. **Borrow a Book** - Demonstrate borrowing system
6. **Return a Book** - Show return functionality
7. **Admin Panel** - Show Django admin features

### Tips:
- Add 5-10 sample books with different genres
- Create 3-4 authors
- Add 2-3 genres
- Borrow a few books to show the system working
- Show the search and filter features

## Troubleshooting

**Issue**: Static files not loading
- Solution: Make sure you're running `python manage.py runserver` from the project root

**Issue**: Images not uploading
- Solution: Create a `media` folder in the project root if it doesn't exist automatically

**Issue**: Database errors
- Solution: Delete `db.sqlite3` and run migrations again

## Features Ready for Demo:
✅ Dark-themed UI
✅ Book management (CRUD)
✅ Author management
✅ Genre management
✅ Borrowing system
✅ Search and filter
✅ Image uploads
✅ Responsive design
✅ Admin panel

Good luck with your presentation! 🚀

