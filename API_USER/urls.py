from django.conf.urls import url
from .views import UserRegistrationView
from .views import UserLoginView
from django.urls import path, include

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    ]