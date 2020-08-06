from django.conf.urls import url
from API_PROFILE.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    ]
