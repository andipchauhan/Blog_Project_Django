# Blog_Project_Django

# Useful commands to run the project
python -m venv venv
pip install -r requirements.txt
python manage.py runserver

# Hosting on AWS

- Django is a framework and not a web server, runserver command runs a development only server not optimcal for production

- wsgi and asgi will work as entrypoints for incomign requests

- Django doesn't serve static files automatically(CSS, user uploads), hence we need to configure the static setting in global URLs
But this approach is not ideal for performance
Instead setup a web server to serve static file and django application
Or use a dedicated server/service to serve the static files

- Configure settings.py to hide secret key using .env file and set DEBUG = False

- sqlite3 alternatives for larger websites with heavier traffic

