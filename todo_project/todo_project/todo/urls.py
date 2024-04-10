from django.urls import path
from .views import TodoListView, TodoDetailView, user_login

urlpatterns = [
    path('login/', user_login, name='login'),
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
]
