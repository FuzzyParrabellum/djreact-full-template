from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.users.models import User
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
