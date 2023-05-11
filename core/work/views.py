from django.shortcuts import render
from api.models import Work
from rest_framework import viewsets
from work import serializers
from rest_framework import permissions

class WorkViewSet(viewsets.ModelViewSet, permissions.IsAdminUser):
    serializer_class = serializers.WorkDetailsSerializer
    queryset = Work.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.WorkSerializer
        return self.serializer_class
    
