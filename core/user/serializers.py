from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'user_type']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, data):
        return get_user_model().objects.create_user(**data)
    
    def update(self, instance, data):
        password = data.pop('password', None)
        user = super().update(instance, data)

        if password:
            user.set_password(password)
            user.save()

        return user
    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'user_type']
