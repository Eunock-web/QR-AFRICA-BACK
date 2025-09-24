from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    
    TYPE_STANDARD = "standard"
    TYPE_PREMIUM = "premium"
    
    TYPE_ABONNEMENT = [
        (TYPE_STANDARD , "standard")
        (TYPE_PREMIUM , "premium")
    ]
    
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    telephone = models.IntegerField()
    type_abonnement = models.CharField(max_length = 100, choices = TYPE_ABONNEMENT, default = TYPE_STANDARD)
    is_superuser = models.BooleanField (default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profil = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add= True)
    last_login = models.DateTimeField(auto_now = True)
    
    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()
    
    @property
    def __str__(self):
        return self.email
    
    def tokens(self):
        pass
    
    

class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" {self.user.firstname}-passcode "