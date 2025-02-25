from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name="index"),
    # that route could be any string, that we are going to give a variable name 'name':
    path("<str:name>", views.greet, name='greet'),
    path("brain", views.brain, name="brain"),
    path("david", views.david, name='david')
]