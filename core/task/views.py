from django.shortcuts import render
from api.models import Task
from rest_framework import viewsets, permissions
from task import serializers

# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.TaskDetailsSerializer
#     queryset = Task.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return serializers.TaskSerializer
#         return self.serializer_class
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests without any check
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write permissions only if the user is the owner of the task
        return obj.owner == request.user

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TaskSerializer
        return serializers.TaskDetailsSerializer

    def get_permissions(self):
        """
        Set permissions based on serializer used in the request.
        """
        serializer_class = self.get_serializer_class()
        if serializer_class == serializers.TaskSerializer:
            return []
        elif serializer_class == serializers.TaskDetailsSerializer:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)