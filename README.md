# Django Blog

A clean, modern blogging platform built with Django.

## Features

- **Blog Posts** - Create and publish posts with categories, tags, and featured images
- **Categories & Tags** - Organize your content with a flexible taxonomy system
- **Comments** - Readers can leave comments with moderation support
- **Search** - Full-text search across all posts
- **Responsive Design** - Looks great on desktop, tablet, and mobile
- **Admin Dashboard** - Manage all content through Django's built-in admin
- **SEO-Friendly** - Clean URLs with slugs, semantic HTML

## Quick Start

### 1. Install Dependencies

```bash
# Create a virtual environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Set Up the Database

```bash
# Run migrations
python manage.py migrate

# Create a superuser to access the admin
python manage.py createsuperuser
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see your blog.
Visit http://127.0.0.1:8000/admin/ to log in and manage content.

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

## Adding Content

1. Log in to the admin panel at `/admin/`
2. First, create **Categories** and **Tags**
3. Then create **Posts** - set the status to "Published" to make them visible
4. Comments submitted by readers will appear in the admin for approval

## Customization

### Change the Blog Name
Edit `django_blog/settings.py` and update the site name in templates.

### Modify Styles
Edit `blog/static/blog/css/style.css` - the CSS uses CSS variables at the top for easy theming.

### Add New Pages
1. Create a new template in `blog/templates/blog/`
2. Add a view in `blog/views.py`
3. Add a URL pattern in `blog/urls.py`
4. Link to it in `blog/templates/blog/base.html`

### Change Posts Per Page
Edit the `POSTS_PER_PAGE` setting in `django_blog/settings.py`.

## Deployment

Before deploying to production:

1. Change `SECRET_KEY` in `settings.py` to a secure random value
2. Set `DEBUG = False`
3. Add your domain to `ALLOWED_HOSTS`
4. Set up a proper database (PostgreSQL recommended)
5. Configure a web server (Gunicorn + Nginx)
6. Set up static file serving with `python manage.py collectstatic`

## License

This project is open source. Feel free to use and modify it as you like!
