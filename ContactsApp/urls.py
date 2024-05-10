from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-details/', views.get_user_details, name='user-details'),  # Renomeando a rota para obter detalhes do usuário
    path('useregist/', views.user_registration, name='user-registration'),
    path('login/', views.user_login, name='login'),  # Adicionando a rota de login
    path('add_contact/', views.add_contact, name='add_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact),
    path('contacts/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.list_users, name='list_users'),
]

