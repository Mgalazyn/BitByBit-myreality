from rest_framework import serializers
from api.models import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['name']

class WorkDetailsSerializer(serializers.ModelSerializer):
    class Meta(WorkSerializer.Meta):
        fields = WorkSerializer.Meta.fields + ['tasks']