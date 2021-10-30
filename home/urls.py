from django.urls import path
from home import views

urlpatterns = [
    path("", views.task, name="task"),
    path("update/<int:pk>", views.updateTask, name="update"),
    path("delete/<int:pk>", views.deleteTask, name="delete"),
    path("complete/<int:pk>", views.completeTask, name="complete"),
]