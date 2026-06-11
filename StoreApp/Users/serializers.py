from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'date_joined',
                  'email',
                  'user_info',
                  'phone_number',
                  'last_login'
                  ]