# Kbuy Store
## Tools Used 
 
Django, MySQL, Data Grip, Dj REST Framework, Dj Admin, Dj ORM, Docker, Redis, Celery, PyTest, JWT, Locust, Silk, Heroku

## Features 
 
User authentication, order processing, database management, RESTful APIs, file uploads, email notifications, background jobs, caching, automated testing, performance testing, static asset management
 
## Documentation links 

Model field: https://docs.djangoproject.com/en/5.1/ref/models/fields/  

The QuerySet API in Django is the interface used to interact with the database using Django's ORM (Object-Relational Mapper). It allows you to retrieve, filter, update, and delete records from your database using Python instead of raw SQL.  
  
QuerySet API: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#field-lookups  
  
Database Functions: https://docs.djangoproject.com/en/5.1/ref/models/database-functions/  
  
Admin site: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#modeladmin-options  
  
Validators: https://docs.djangoproject.com/en/5.1/ref/validators/ 
 
Expression class: Value, F, Func, Aggregate, ExpressionWrapper 
 
## Notes 
 
API - Application Programming Interface 
 
RESTful - Representation State Transfer describes the design/architecture/rules for the WWW. Benefits: fast, scalable, reliable, easy to understand, easy to change. Key concepts: Resources, Representation, HTTP Methods. 
 
Resources - object, data, or entity that can be identified and manipulated through interactions with API (Product, Collection, Cart). Can be located/identified via URLs and acted upon by HTTP methods. 
 
Resource Representation - refers to how a resource is presented or formatted when it is sent from the server to the client or vice versa. Common formats: HTML, XML, JSON. 
 
HTTP Methods - the actions that clients can perform on resources in a RESTful API. Methods: Get, Post (create), Put (update/create), Patch (update partially), Delete. 
 
Serializer - a component that converts complex data types (like Django models or querysets) into Python data types (dictionaries) that can be easily rendered into JSON, XML, or other content types.

Serializer fields: https://www.django-rest-framework.org/api-guide/fields/ 
 
Serializing relationships: primary key, string, nested object, hyperlink (p2 l13) 
 
Function-Based api Views for very simple APIs (one or two request types). 
Class-Based api Views - for structured, reusable APIs that need customization. 
Generic Views - when working with standard CRUD operations. 
 
Mixins: https://www.django-rest-framework.org/api-guide/generic-views/#mixins
 
Filters/How to create custom filters: https://django-filter.readthedocs.io/en/stable/ 
 
Building an API: Serializer -> View -> Route 
 
Djoser - third-party package that simplifies the implementation of authentication-related functionality, particularly for building RESTful APIs.

Djoser: https://djoser.readthedocs.io/en/latest/
 
Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/ 
 
JWT: https://jwt.io 
 
Run Server, Redis nad Celery in 3 different terminals
 
$ python manage.py run
 
$ docker run -p 6379:6379 redis
 
$ celery -A storefront worker
 
Every test should have 3 parts, or AAA - Arrange, Act, Assert.
 
Python logging: https://docs.python.org/3/library/logging.html 
