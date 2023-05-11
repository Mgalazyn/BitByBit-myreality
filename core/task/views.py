from django.shortcuts import render
from api.models import Task
from rest_framework import viewsets
from task import serializers

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskDetailsSerializer
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TaskSerializer
        return self.serializer_class