from django.urls import path
from app.views import home


urlpatterns = [
    # Home page
    path("", home, name="home"),
]