from rest_framework import serializers
from notes.models import home13

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = home13
        fields = '__all__'