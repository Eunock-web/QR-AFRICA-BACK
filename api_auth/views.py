from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import  AllUserSerializer, UpdateUserSerializer, UserSerializer,UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework.permissions import AllowAny
# from .utils import send_otp_email

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "statuts": True,
                "message": "Utilisateur créé avec succès",
                "user": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

# class LogoutView(APIView):
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "statuts": True,
                    "message": "Utilisateur connecté avec succès",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response({"error": "Invalid credentials"}, status=400)
        
        
        
    
# Endpoint pour récupérer l'utilisateur connecté
class get_user(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    

#Liste des utilisateurs

class AllUsers(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    
    