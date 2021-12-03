from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/', views.delete, name='delete'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('update/<int:id>', views.update, name='update'),
    path('filter/<str:kwrd>', views.filter, name='filter'),
    path('sort/<int:value>', views.sort, name='sort')
]