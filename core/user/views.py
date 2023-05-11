from django.shortcuts import render
from rest_framework import generics, viewsets
from user.serializers import UserSerializer, UserDetailsSerializer
from user.permissions import AdminPermissions
from api.models import User


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AdminPermissions]

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserDetailsSerializer
        return self.serializer_class