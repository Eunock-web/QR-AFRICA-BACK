from django.shortcuts import render
from rest_framework.generics import GenericApiView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .utils import send_otp_email

# Create your views here.

class RegisterUserView(GenericApiView):
    
    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data = user_data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            user = serializer.data
            send_otp_email(user['email'])
            return Response({
                'data':user,
                'message':'User Create Successfully'
            },status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    