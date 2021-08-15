from rest_framework import serializers
from .models import ToDoDetails


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoDetails
        fields = ['title', 'data']
