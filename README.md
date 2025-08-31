# Blog_Project_Django

When I activate a virtual environment, it works globally within my shell session. I can navigate to any folder, even restricted ones, and any dependencies I install will still be stored inside the virtual environment without affecting those folders. Also, all commands will use the dependencies installed in the virtual environment.

# Useful commands to run the project
python -m venv venv
pip install -r requirements.txt
python manage.py runserver

# Hosting

- Django is a framework and not a web server, runserver command runs a development only server not optimcal for production

- wsgi and asgi will work as entrypoints for incomign requests

- Django doesn't serve static files automatically(CSS, user uploads), hence we need to configure the static setting in global URLs
But this approach is not ideal for performance
Instead setup a web server to serve static file and django application
Or use a dedicated server/service to serve the static files

- Configure settings.py to hide secret key using .env file and set DEBUG = False

- sqlite3 alternatives for larger websites with heavier traffic


# Hosting on AWS (platform = python and upload your code)

1. add this in **settings.py** - STATIC_ROOT = BASE_DIR / "staticfiles"
2. python manage.py collectstatic
<!-- Make sure these collected django files also get served as django does not by default -->
3. (1st approach) add in **urls.py** - "+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
4. Create your superuser
5. Make sure to make and run migartions
6. So database is initialised, containing basic database schema and the superuser
<!-- add the domain or IP your website will be served on for APP_HOST or use environment variables  -->
7. **settings.py** - ALLOWED_HOSTS = getenv("APP_HOST", "localhost").split(",")
 - Also add env variables for secret key, DEBUG, DB, etc also
```
from os import getenv
from dotenv import load_dotenv
load_dotenv()
```
- .env file at same level as manage.py
8. AWS Elastic Beanstalk
9. Add at same level as manage.py .ebextensions folder > django.config file
```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: my_site.wsgi:application
```
10. Manually select and zip the folders to be uploaded
 - NOT the .env and static folder (since compiled static files are in staticfiles folder)
11. Give dummy value to beanstalk env vars APP_HOST
12. Once deployed copy the url and set in APP_HOST (omit http and slash)
    - APP_HOST in environment properties of AWS Beanstalk
    - IS_DEVELOPMENT
    - SECRET_KEY
13. For SSL, we can use a load balancer (PAID)
14. Route53 for csutom domains (PAID)
<!-- Using a different database : PostgreSQl-->
15. Create AWS RDS DB with PostgreSQL engine type in sandbox/free tier
16. Also set master username and password and create a new VPC
17. **settings.py** DATABASES
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'djangoblog',
        'PASSWORD': 'djangoblog',
        'HOST': 'django-blog.c3uw6pxedh7p.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}
```
 - **use env variables instead of directly exposing username, password and sensetive data in settings.py**
 - **doesn't matter here as these are sandbox creds only for development**

<!-- Below command will connect to DB and create necessary tables-->
18. python manage.py migrate
19. python manage.py createsuperuser
20. python manage.py runserver
21. Upload and deploy updated code on beanstalk(omit db.sqlite3 this time)
22. Edit inbound rules for RDS security group in VPC and open to everyone(as password protection is there)
    - Reupload updated codebase zip
<!-- Serving static files separately -->
23. In .ebextensions add file static-files.config so beanstalk will change configuration of nginx server to serve static files differently
 ```
 option_settings:
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles
    /files: uploads
 ```
 - remove + static() from urls.py
24. Reupload updated codebase zip
25. Django server will now not serve the static files as it is ineffiecient and this would instead be done by nginx

<!-- Static files can also be served by a whole other server - AWS S3 for example -->
