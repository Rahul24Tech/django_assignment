from rest_framework import generics, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
    return render(request, 'index.html')