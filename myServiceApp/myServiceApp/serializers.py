from rest_framework import serializers
from .models import services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = services
        fields = ['text', 'pic']
