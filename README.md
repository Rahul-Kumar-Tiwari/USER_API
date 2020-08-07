***Change these Dependencies in Setting.py File*** <br />
*DATABASES = { <br />
    'default': {<br />
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br />
        'NAME': 'USER_DATA',<br />
        'USER': 'postgres',<br />
        'PASSWORD': 'rahul',<br />
        'HOST': 'localhost',<br />
        'PORT': '',<br />
    }<br />
}*<br /><br />

***Change these Dependencies in Settings.py File for reciving the password reset token on mail*** <br />
*EMAIL_HOST="smtp.gmail.com"<br />
EMAIL_PORT=587<br />
EMAIL_HOST_USER='abc@gmail.com'<br />
EMAIL_HOST_PASSWORD='abcxyz'<br />
EMAIL_USE_TLS=True*<br />

Otherwise uncomment "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'" this in settings.py file for reciving the password reset token on console. <br /><br/>

**Signup API**<br />
***Start postman create a new request for http://127.0.0.1:8000/api/signup Select method as Post, goto body and select raw and the JSON.<br />
In body enter the JSON in the following format and hit the request***<br />
*{<br />
 "email":"rahul@gmail.com",<br />
 "password":"rahul123",<br />
 "profile": {<br />
        "first_name": "Rahul",<br />
        "last_name": "kumar",<br />
        "phone_number": "1234567891",<br />
        "age": 15,<br />
        "user_type": "Teacher"<br />
 }<br />
}*<br />

**Signin API**<br />
***Start postman create a new request for http://127.0.0.1:8000/api/signin Select method as Post, goto body and select raw and the JSON.<br />
In body enter the JSON in the following format and hit the request***<br />
*{<br />
 "email":"rahul@gmail.com",<br />
 "password":"rahul123"<br />
}*<br />


**Reset Password API**<br />
***Start postman create a new request for http://127.0.0.1:8000/api/password_reset/ Select method as Post, goto body and select raw and the JSON.<br />
In body enter the JSON in the following format and hit the request***<br />
*{<br />
 "email":"rahul@gmail.com",<br />
}*<br />
***Copy link which is in email, will be similar to /api/password_reset/?token=339e80fe05e5ca9fc74799213f81a093d1f***<br />

***Now copy that token which comes in email and and post token and password to /api/password_reset/confirm/ api url.***<br />
*{<br />
    "token":"3339e80fe05e5ca9fc74799213f81a093d1f",<br />
    "password":"Password@123"<br />
}*<br /><br />

**Profile Retrive API**<br />
***Start postman create a new request for http://127.0.0.1:8000/api/profile Select method as GET, <br />
goto Authorization and select Bearer Token from TYPE, paste the token and hit the request***<br /><br /><br />



**Thank You**




