from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # ['username', 'email', 'phone_number', 'first_name', 'last_name']
        # Adjust the fields list to include any
        # other fields you want to serialize
