from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                         BaseUserManager, 
                                         PermissionsMixin)
 

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
    USER_TYPE_CHOICES = (
        ('basic', 'Basic'),
        ('admin', 'Admin')
    )

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default='basic', max_length=5)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    #exchaning default username's field for email address
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Work(models.Model):
    name = models.CharField(max_length=255)
    tasks = models.ManyToManyField('Task', related_name='works')

    def __str__(self):
        return self.name