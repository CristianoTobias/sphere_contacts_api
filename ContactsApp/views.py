from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    # Verificar se o cookie de sessão está presente
    if 'user_id' in request.session:
        frontend_user = request.session['user_id']
    else:
        frontend_user = None  # Não temos informações do usuário do frontend para exibir no frontend

    # Verificar se há um usuário autenticado no backend
    backend_user = request.user if request.user.is_authenticated else None

    # Renderizar o template com as informações dos usuários do frontend e do backend
    return render(request, 'home.html', {'frontend_user': frontend_user, 'backend_user': backend_user})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_contacts(request):
    if not request.user.is_authenticated:
        return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

    # Buscar os contatos do usuário logado
    contacts = Contacts.objects.filter(user=request.user)
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_contact(request):
    if request.user.is_authenticated:
        default_user = request.user
    else:
        default_user = None

    data = request.data.copy()  # Cria uma cópia mutável dos dados da requisição
    data['user'] = default_user.id if default_user else None

    serializer = ContactsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_details(request):
    # if request.user.is_authenticated:
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # else:
    #     return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_registration(request):
    serializer = UserRegSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Corrigido o retorno do erro


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_contact(request, pk):
    try:
        contact = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_contact(request, pk):
    try:
        contact = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        print("Received data:", request.data)  # Adicione esta linha para logar os dados recebidos
        serializer = ContactsSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("Validation errors:", serializer.errors)  # Adicione esta linha para logar os erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    