from djoser.serializers import UserCreateSerializer as BaseUserCreateClass
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateClass):
    class Meta(BaseUserCreateClass.Meta):
        fields = ['id', 'username', 'password', 
                  'email', 'first_name', 'last_name']
        

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']