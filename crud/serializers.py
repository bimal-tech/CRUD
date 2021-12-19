from rest_framework import serializers
from .models import operation


class operationSerializer(serializers.ModelSerializer):
    class Meta:
        model = operation
        field = '__all__'
