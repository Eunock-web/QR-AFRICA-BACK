from rest_framework import permissions
from .models import WIFI, QrCode
from rest_framework import generics, serializers
from .serializers import WifiSerializer
from rest_framework.response import Response

class WifiCreateView(generics.CreateAPIView):
    queryset = WIFI.objects.all()
    serializer_class = WifiSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        qr_code = QrCode.objects.create(
            type_qr_code="wifi",   
            user=self.request.user
        )
        serializer.save(qr=qr_code)
        if serializer.is_valid():
            return Response({"statuts": True, "data": serializer.data, "message": "QR code creer avec succes"})
        else:
            return Response({"statuts": False, "data": serializer.errors, "message": "Erreur lors de la creation"})

class WifiRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WIFI.objects.all()
    serializer_class = WifiSerializer
    
    def perform_retrieve(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data, "message":"QR code recuperer avec succes"})

class WifiListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WIFI.objects.all()
    serializer_class = WifiSerializer
    
    
    def perform_list(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data})

class WifiUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WIFI.objects.all()
    serializer_class = WifiSerializer
    
    def perform_update(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data, "message":"QR code mis a jour avec succes"})


class WifiDestroyView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WIFI.objects.all()
    serializer_class = WifiSerializer
    
    def perform_destroy(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data, "message":"QR code supprimer avec succes"})
    
