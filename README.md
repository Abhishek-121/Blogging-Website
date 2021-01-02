# Blogging-Website

This a Blogging website in which user can post their blog and other people as well as the author have the permission to like and comment on their blog as well as have the functionality in which author can edit their blog .



Requirements :
Django must be installed in your system otherwise use command : pip install django
Python also required 
Install some libraries like Pillow for image , Reverse, crispy forms etc.

==> While you create models after registering your models in admin.py use the following 2 commands :
    1. python manage.py makemigrations- Used whenever you make a change to a model, even if it is updating the description on a field.
    2. python manage.py migrate - We will need to migrate whenever new migrations are available that have not yet been applied to the data in the current instance.


Steps to run this project on Your System :

Step1 : First clone this project.
Step2 : Create the virtual environment using commands - 
        virtualenv env_name 
        env_name/Scripts/Activate 
Step3 : Run the command : python manage.py runserver


