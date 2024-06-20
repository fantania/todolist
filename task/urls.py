from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.edit_task, name= 'edit_task'),
]