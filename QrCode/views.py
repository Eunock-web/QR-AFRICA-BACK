from django.shortcuts import render
from rest_framework import generics
from .serializer import LienSerializer
from .models import Lien

# Create your views here.

"""
    -class pour le CRUD concernant le lien
"""
class CreateLien(generics.CreateAPIView):
    queryset = Lien.objects.all()
    serializer_class = LienSerializer

class DetailLien(generics.RetrieveAPIView):
    queryset = Lien.objects.all()
    serializer_class = LienSerializer

class ListLien(generics.ListAPIView):
    queryset = Lien.objects.all()
    serializer_class = LienSerializer


class UpdateLien(generics.UpdateAPIView):
    queryset = Lien.objects.all()
    serializer_class = LienSerializer

class DestroyLien(generics.DestroyAPIView):
    queryset = Lien.objects.all()
    serializer_class = LienSerializer
