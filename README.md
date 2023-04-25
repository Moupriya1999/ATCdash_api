# ATCdash_api

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

  1. Python
  2. Django
  3. django-allauth
  4. django-auditlog
  5. djangorestframework
  6. mysqlclient
  7. Pillow
  8. oauthlib
  9. djangorestframework-simplejwt
 
 # <b>Usage</b>
   Run the below commands after setting up the project
   
   1.python manage.py makemigrations

   2.python manage.py migrate

   3.python manage.py runserver
   
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/ 

