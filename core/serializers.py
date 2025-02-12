from djoser.serializers import UserCreateSerializer as BaseUserCreateClass
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateClass):
    class Meta(BaseUserCreateClass.Meta):
        fields = ['id', 'username', 'password', 
                  'email', 'first_name', 'last_name']