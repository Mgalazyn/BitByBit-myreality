from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from user.serializers import UserSerializer, UserDetailsSerializer
from user.permissions import AdminPermissions
from api.models import User
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import reverse
from django.contrib.auth import authenticate, login


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = authenticate(request=request, username=request.data['email'], password=request.data['password'])
            login(request, user)
            # Redirect to user list 
            return redirect(reverse('user:user-list'))
        return response


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

