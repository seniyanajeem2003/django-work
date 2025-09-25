from rest_framework import serializers
from .models import class13

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = class13
        fields = '__all__'