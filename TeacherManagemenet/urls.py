from django.urls import path

from . import views

urlpatterns = [
    path('createTeacher/', views.teacherCreation, name='teacherCreation'),
]
