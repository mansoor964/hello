from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name="index"),
    path("brain", views.brain, name="brain")
]