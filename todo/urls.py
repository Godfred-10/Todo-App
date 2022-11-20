from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>/', views.completeTodo, name='complete'),
    path('deleteCompleted', views.deleteComplete, name='deletecomplete'),
    path('deleteAll', views.deleteAll, name='deleteall'),
]