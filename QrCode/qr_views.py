from rest_framework import permissions
from .models import QrCode
from rest_framework import generics
from rest_framework.response import Response
from .serializers import QrSerializer

#Classe pour recuperer touts les qr codes
class AllQrCodesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QrSerializer

    def get_queryset(self):
        return QrCode.objects.filter(user=self.request.user)
    
    

#Classe pour recuperer les qr codes par type
class QrCodeByTypeListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QrSerializer

    def get_queryset(self):
        qr_type = self.kwargs.get("type")  # récupéré depuis l’URL
        return QrCode.objects.filter(type_qr_code=qr_type, user=self.request.user)
