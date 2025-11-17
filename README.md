# 📚 Library Management System

A modern, feature-rich Library Management System built with Django and Python. This system provides a complete solution for managing books, authors, genres, and tracking book borrowings with a beautiful dark-themed user interface.

![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [User Roles](#-user-roles)
- [Security Features](#-security-features)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🔐 Authentication & Authorization
- **User Registration & Login**: Secure user authentication system with email validation
- **Role-Based Access Control**: 
  - **Admins**: Full CRUD operations on all resources
  - **Regular Users**: Browse, search, borrow, and return books
- **Session Management**: Secure login/logout functionality
- **Password Security**: Django's built-in password hashing and validation

### 📖 Book Management
- **Complete CRUD Operations**: Create, Read, Update, Delete books (Admin only)
- **Book Content Upload**: Upload PDF/DOC/DOCX/TXT/EPUB files for digital reading
- **Cover Image Upload**: Upload book cover images with live preview
- **Content Access Control**: Users can only view/download content after borrowing
- **Advanced Search**: Search by title, author, ISBN, or description
- **Genre Filtering**: Filter books by genre with dropdown selector
- **Status Management**: Automatic status updates (Available/Borrowed/Reserved)
- **Pagination**: Efficient handling of large book collections

### 👤 Author & Genre Management
- **Author Management**: Add authors with biography and birth date
- **Genre Management**: Organize books by categories
- **Admin-Only Creation**: Only admins can add authors and genres
- **Author Details**: View author biography and all their books
- **Genre Statistics**: See book count per genre

### 📋 Borrowing System
- **Borrow Books**: Users can borrow available books with due date tracking
- **Return Books**: Easy return functionality with automatic availability updates
- **Borrowing History**: Track all borrowings (users see only their own)
- **Automatic Updates**: Book availability updates automatically on borrow/return
- **Due Date Tracking**: Track due dates for borrowed books
- **Borrowing Filters**: Filter by active/returned status

### 🎨 User Interface
- **Dark Theme**: Beautiful, modern dark-themed interface
- **Animated Background**: Smooth gradient animations with radial overlays
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Image Previews**: Preview book covers before upload
- **Intuitive Navigation**: Easy-to-use navigation menu with active state indicators
- **Form Validation**: Real-time form validation with error messages
- **Success/Error Messages**: User-friendly feedback messages

### 🔍 Additional Features
- **Admin Panel**: Full Django admin integration for backend management
- **File Management**: Secure file upload and storage system
- **Search Functionality**: Advanced search across multiple fields
- **Statistics Dashboard**: Home page with library statistics
- **Recent Books**: Display recently added books on homepage

---

## 🖼️ Screenshots

### Home Page
- Statistics dashboard showing total books, authors, genres, and availability
- Quick action buttons for common tasks
- Recent books display

### Book Management
- Book listing with search and filter options
- Book detail page with cover image and content access
- Add/Edit book forms with image and file upload

### User Features
- User registration and login pages
- My Borrowings page showing user's borrowing history
- Content viewing and downloading (after borrowing)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

2. **Create a virtual environment (Recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (Admin account)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
   - **Main Website**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

> 📖 **For detailed setup instructions, see [GUIDANCE.md](GUIDANCE.md)**

---

## 📖 Usage Guide

### For Administrators

#### Getting Started
1. **Login** with your admin credentials at http://127.0.0.1:8000/admin/
2. **Add Authors**: Navigate to Authors → Add New Author
3. **Add Genres**: Navigate to Genres → Add New Genre
4. **Add Books**: Navigate to Books → Add New Book

#### Adding a Book
1. Go to **Books** → **Add New Book**
2. Fill in book details:
   - Title (required)
   - Author (select from dropdown or add new)
   - Genre (optional, select from dropdown)
   - ISBN (optional)
   - Description (optional)
   - Published Date (optional)
   - Total Copies (required)
   - Available Copies (required)
3. Upload files:
   - **Cover Image**: Upload a book cover (JPG, PNG)
   - **Content File**: Upload book content (PDF, DOC, DOCX, TXT, EPUB)
4. Click **Save Book**

#### Managing Borrowings
- View all borrowings in the **Borrowings** section
- Filter by active/returned status
- Return books on behalf of users if needed

### For Regular Users

#### Registration & Login
1. **Register**: Go to http://127.0.0.1:8000/register/
   - Fill in username, email, and password
   - Click **Register**
2. **Login**: Go to http://127.0.0.1:8000/login/
   - Enter credentials and click **Login**

#### Browsing & Searching Books
1. **Browse Books**: Navigate to **Books** from the menu
2. **Search**: Use the search bar to find books by:
   - Title
   - Author name
   - ISBN
   - Description
3. **Filter**: Use the genre dropdown to filter by category

#### Borrowing a Book
1. Find a book you want to borrow
2. Click **Borrow** button (or go to book detail page)
3. Fill in the due date
4. Click **Borrow Book**
5. The book is now in your borrowing list

#### Accessing Book Content
1. **Borrow the book first** (required)
2. Go to **My Borrowings** or click on the book
3. On the book detail page, you'll see:
   - **View Content**: Opens PDF/document in browser
   - **Download**: Downloads the file to your device
4. Note: Content access is only available for borrowed books

#### Returning a Book
1. Go to **My Borrowings**
2. Find the book you want to return
3. Click **Return** button
4. Confirm the return
5. Book availability updates automatically

---

## 📁 Project Structure

```
library-management-system/
├── library/                      # Main Django app
│   ├── migrations/              # Database migrations
│   │   ├── 0001_initial.py
│   │   └── 0002_book_content_file.py
│   ├── templates/               # HTML templates
│   │   └── library/
│   │       ├── base.html        # Base template with navigation
│   │       ├── home.html        # Home page with statistics
│   │       ├── book_list.html   # Book listing page
│   │       ├── book_detail.html # Book detail page
│   │       ├── book_form.html   # Add/Edit book form
│   │       ├── book_confirm_delete.html
│   │       ├── author_list.html # Author listing
│   │       ├── author_detail.html
│   │       ├── author_form.html
│   │       ├── genre_list.html  # Genre listing
│   │       ├── genre_form.html
│   │       ├── borrowing_list.html
│   │       ├── borrowing_form.html
│   │       ├── borrowing_return.html
│   │       ├── login.html       # Login page
│   │       └── register.html    # Registration page
│   ├── models.py               # Database models (Book, Author, Genre, Borrowing)
│   ├── views.py                # View functions and business logic
│   ├── urls.py                 # URL routing
│   ├── forms.py                # Form definitions
│   └── admin.py                # Admin configuration
├── library_project/            # Django project settings
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── static/                     # Static files
│   └── css/
│       └── style.css           # Main stylesheet (dark theme)
├── media/                      # User-uploaded files (not in git)
│   ├── book_covers/           # Book cover images
│   └── book_content/          # Book content files (PDFs, etc.)
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── GUIDANCE.md                 # Detailed setup guide
└── .gitignore                  # Git ignore rules
```

---

## 🗄️ Database Models

### Book Model
- **Fields**: title, author (FK), isbn, genre (FK), description, published_date, total_copies, available_copies, status, cover_image, content_file, created_at, updated_at
- **Relationships**: Many-to-One with Author, Many-to-One with Genre, One-to-Many with Borrowing
- **Features**: Automatic status calculation based on availability

### Author Model
- **Fields**: name, bio, birth_date, created_at
- **Relationships**: One-to-Many with Book

### Genre Model
- **Fields**: name, description, created_at
- **Relationships**: One-to-Many with Book

### Borrowing Model
- **Fields**: book (FK), borrower_name, borrower_email, borrower_phone, borrow_date, return_date, due_date, is_returned, created_at, updated_at
- **Relationships**: Many-to-One with Book
- **Features**: Automatic copy management on borrow/return

---

## 🛠️ Technologies Used

### Backend
- **Django 4.2.7**: High-level Python web framework
- **Python 3.8+**: Programming language
- **SQLite**: Default database (can be changed to PostgreSQL/MySQL)

### Frontend
- **HTML5**: Markup language
- **CSS3**: Styling with dark theme and animations
- **JavaScript**: Client-side interactivity (image preview)

### Libraries
- **Pillow 10.1.0**: Image processing library for cover images

---

## 👥 User Roles

### 🔴 Admin Users

**Capabilities:**
- ✅ Create, edit, delete books
- ✅ Create authors and genres
- ✅ View all borrowings (all users)
- ✅ Access Django admin panel
- ✅ View/download all book content (without borrowing)
- ✅ Manage all aspects of the system

**How to Create:**
```bash
python manage.py createsuperuser
```

### 🔵 Regular Users

**Capabilities:**
- ✅ Register and login
- ✅ Browse and search books
- ✅ View book details
- ✅ Borrow books
- ✅ View/download content of **borrowed books only**
- ✅ Return books
- ✅ View their own borrowing history
- ❌ Cannot add/edit/delete books
- ❌ Cannot add authors/genres
- ❌ Cannot access admin panel

**Registration:**
- Go to http://127.0.0.1:8000/register/
- Fill in registration form
- Login with credentials

---

## 🔒 Security Features

- **Authentication Required**: Login required for borrowing and content access
- **Borrowing Verification**: Users can only access content of borrowed books
- **Admin Protection**: CRUD operations restricted to admin users
- **CSRF Protection**: Django's built-in CSRF protection on all forms
- **Secure File Uploads**: Validated file types and secure storage
- **Password Hashing**: Django's PBKDF2 password hashing algorithm
- **Session Security**: Secure session management

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "No such table: library_book"
**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Issue: Static files not loading
**Solution:**
- Ensure you're running server from project root
- Check that `static/css/style.css` exists
- Restart the server

#### Issue: Images not uploading
**Solution:**
- Check that `media/` directory exists
- Ensure `media/book_covers/` directory exists
- Verify file permissions

#### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution:**
- Activate virtual environment
- Run `pip install -r requirements.txt`

#### Issue: Cannot access content after borrowing
**Solution:**
- Verify the book has a content file uploaded
- Check that borrowing email matches user email
- Ensure borrowing is not marked as returned

> 📖 **For more troubleshooting tips, see [GUIDANCE.md](GUIDANCE.md)**

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. **Fork the repository**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 Python style guide
- Write clear commit messages
- Add comments for complex code
- Test your changes before submitting

---

## 📝 License

This project is created for educational purposes. Feel free to use and modify as needed.

---

## 👨‍💻 Author

Created as a college project demonstrating Django web development skills.

**Features Demonstrated:**
- Django framework proficiency
- Database design and relationships
- User authentication and authorization
- File upload and management
- RESTful URL design
- Template inheritance
- Form handling and validation
- Security best practices

---

## 🙏 Acknowledgments

- **Django Framework**: For the amazing web framework
- **Python Community**: For continuous support and resources
- **All Contributors**: For improvements and suggestions

---

## 📞 Support

For issues, questions, or contributions:
- **Open an issue** on GitHub
- **Check [GUIDANCE.md](GUIDANCE.md)** for detailed documentation
- **Review Django documentation**: https://docs.djangoproject.com/

---

## 🎯 Project Status

✅ **Fully Functional** - All features implemented and tested

**Current Version**: 1.0.0

**Last Updated**: November 2025

---

<div align="center">

**Made with ❤️ using Django and Python**

⭐ **Star this repo if you find it helpful!** ⭐

</div>
