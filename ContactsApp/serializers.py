from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

    def create(self, validated_data):
        # Se o campo 'user' não estiver presente nos dados validados,
        # define-o como o usuário 'admin' padrão
        if 'user' not in validated_data:
            default_user = User.objects.get(username='admin')
            validated_data['user'] = default_user
        return super().create(validated_data)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class UserRegSerializer(serializers.Serializer):
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
