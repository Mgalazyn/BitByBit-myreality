from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                         BaseUserManager, 
                                         PermissionsMixin)
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    #manager for users

    def create_user(self, email, password=None, **extra_fields):
        #Function for create, save and run a new user
        if not email:
            raise ValueError('Can\' create user without email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password):
        #Function for creating superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    #creating user model, permissionsmixin for functionality permisisons and fields
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    #exchaning default username for email address
    USERNAME_FIELD = 'email'
