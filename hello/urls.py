from django.urls import path
from . import views
urlpatterns = [
    path("<str:name>", views.home, name="home"),
    path("home",views.index,name="index"),
]