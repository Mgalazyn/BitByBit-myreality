from django.shortcuts import render
from api.models import Work
from rest_framework import viewsets
from work import serializers
from rest_framework.permissions import BasePermission, IsAuthenticated

class SuperuserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WorkDetailsSerializer
    permission_classes = [IsAuthenticated, SuperuserPermission]
    queryset = Work.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.WorkSerializer
        return self.serializer_class
    
