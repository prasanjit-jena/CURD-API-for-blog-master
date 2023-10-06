# Programming Language: Python

# Python's Web Framework: Django

# Database Used: MySQL

## GitHub Profile: https://github.com/Suv-Mohanty/

## Necessary Instructions To Set Up And Run The Application:
1. You need to install python application, django application, djangorestframework, serializers, pymysql (as I have used "MySQL" database). #To install, write on terminal "pip install <app or module name>" and run.
2. Then, run makemigrations and migrate command.
3. My APIToken is c68fbfa177e9d7cdda7a2f28c46ec0253e6691fd
4. You can go 'Postman' to see all the details and the URL is "http://127.0.0.1:8000/posts/" and can perform CRUD operations.

## A Brief Explanation Of My Project
1. This is a project based on a Blog where users can perform CRUD operations like Create, Read, Update and Delete blog posts.
2. First, I created the Django project and Django App.
3. Then in settings, added "<appname>, rest_framework, rest_framework.authtoken" to create Restful API that have authentication policies.
4. Created Model, Serializer, Views that include all CRUD functions and then defined URLs.
5. Created superuser, registered model in admins.py, logged in to admin account and generated token for admin and then added the token to Authorization field in 'Postman'. eg: Token fbead655dc06a1b71258aece42b4d5f81c5ff21e