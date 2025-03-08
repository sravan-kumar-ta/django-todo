from django.urls import path

from todos import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('complete/<int:pk>/', views.todo_complete, name='complete'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]
