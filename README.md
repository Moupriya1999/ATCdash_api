# ATCdash_SupportSquard

<b> This is a project of Adamas Tech Consultancy for monitoring Support System related to SMS (Student Management System) and LMS (Learning Management System)</b>

In this project I have created a responsive dashboard for monitoring Support System, under that I can able to track the below points 

a) <b> Payment Success / Fail:</b> This segment would display the number of successful payments versus the number of failed payments over a given time period. This information
   
b) <b>Payment Success but Registration Fail in SMS:</b> This segment would track the number of successful payments where the customer attempted to register but failed 
   due to an issue with the SMS system. This could help identify any technical issues with the SMS system that may be preventing successful registrations.

c) <b>SMS to LMS Transfer:</b> This segment would track the number of successful student transfers from the SMS system to the LMS. This can help ensure that all 
   relevant data is being transferred correctly and in a timely manner.

d) <b>SMS to Ticketing System:</b> This segment would track the number of successful transfers from the SMS system to the ticketing system. This can help ensure that
   all customer inquiries and issues are being addressed in a timely manner.

e) <b>LMS:</b> This segment would display information related to the Learning Management System, such as the number of users registered, the number of courses offered,
   and the completion rates for different courses. This information can be helpful in identifying any areas that may require improvement or additional resources.

Overall, having a dashboard that tracks these different segments can help ensure that the support system is running smoothly and efficiently, while also providing valuable insights into areas that may require improvement.


# <b>Installation</b>:

 At first download the zip file of this project and extract it. Then open it in a choice of editor. After that install the following packages

  * Python
  * Django
  * django-allauth
  * django-auditlog
  * djangorestframework
  * mysqlclient
  * Pillow
  * oauthlib
  * djangorestframework-simplejwt
  
 <b>OR</b>
 
 Clone using
 ```bash
  https://github.com/Moupriya1999/ATCdash_api.git
 ```
 * Add a new virtual environment to this project (venv). to create venv follow the below commands and copy and paste to your IDE terminal.
```bash
python -m venv venv
```
now to activate venv
```bash
cd venv/Scripts/activate.ps1
```
 ```bash
  pip install -r requirements.txt
  ```
  ```bash
  cd dashboard
 ```
 # <b>Usage</b>
   Fill database name , database password and user in settings.py like
   
 ```bash  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_databse_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
   ```
    Now run make migrations command, running make migrations command will perform Data Migrations to save the "Badges" in the database.
    
    Then migrate to load the operations of Data Migrations in database.
   ```bash 
    python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```
   * Now crete super user using the command: python manage.py createsuperuser

   * Then give username and password for super user

   * Then run the project using the command:
   ```bash
    python manage.py runserver
   ```
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/ 
   
   # API
  * use this url for API: http://127.0.0.1:8000/users/  
  * call API through Postman or your choice of API platform 

