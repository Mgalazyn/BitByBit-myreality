from rest_framework import serializers
from api.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description']

class TaskDetailsSerializer(serializers.ModelSerializer):
    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + ['description', 'owner']