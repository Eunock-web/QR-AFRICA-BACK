from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "telephone",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Veuillez confirmer le mot de passe")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2", None)  # pour éviter l’erreur KeyError
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['email', 'first_name', 'last_name', 'password']
        model = User
        
class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["email", "first_name", "last_name", "telephone"]
        model = User

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['email', 'first_name', 'last_name', 'telephone', 'password', 'type_abonnement', 'profil']
        model = User