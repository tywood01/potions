from django.urls import path
from . import views

app_name = "potion"
urlpatterns = [
    path("", views.home, name="home"),
]
