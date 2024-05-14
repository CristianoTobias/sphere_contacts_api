from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=100, write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            password= validated_data['password']
        )
        return user
    
    class Meta:  # Adicionando a classe Meta
        model = User
        fields = ['username', 'password']  # Especifique os campos que serão incluídos no serializer
