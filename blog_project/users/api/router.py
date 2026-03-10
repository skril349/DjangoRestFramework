from django.urls import path
from .views import RegisterView, UserView

# Creamos las rutas para los endpoints de registro y login de usuarios
urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/me/', UserView.as_view(), name='user'),
    
]

