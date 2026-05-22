# Django Blog
A full-stack blog web application built with Django.
It allows users to create, read, update, and delete blog posts with authentication and a clean 
--
## Features
- User authentication (Register / Login / Logout)
- Create, edit, and delete blog posts
- View all posts and individual post pages
- Comment system (optional)
- User profiles (optional)
- REST API support (if applicable)
- Admin dashboard for content management
--
## 🛠️ Tech Stack
- Python
- Django 
- SQLite 
- HTML, CSS, JavaScript 
- Bootstrap 
- JWT / Session Authentication
--
## Project Structure
```
django_blog/
├── blog/                       # Main blog application
│   ├── admin.py               # Admin configuration
│   ├── forms.py               # Forms (comment, post)
│   ├── models.py              # Data models (Post, Category, Tag, Comment)
│   ├── urls.py                # URL routing for the blog
│   ├── views.py               # View logic
│   ├── static/blog/
│   │   ├── css/style.css      # All styles
│   │   └── js/main.js         # JavaScript for interactions
│   └── templates/blog/
│       ├── base.html          # Base template
│       ├── home.html          # Homepage with featured posts
│       ├── post_list.html     # All posts listing
│       ├── post_detail.html   # Individual post page
│       ├── category_posts.html # Posts filtered by category
│       ├── tag_posts.html     # Posts filtered by tag
│       ├── search_results.html # Search results page
│       └── about.html         # About page
├── django_blog/               # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

