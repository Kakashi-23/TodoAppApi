from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TodoDetailSerializer
from .models import ToDoDetails


# Create your views here.

class TodoDetailList(ListCreateAPIView):
    serializer_class = TodoDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return ToDoDetails.objects.filter(owner=self.request.user)
