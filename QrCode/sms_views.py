from rest_framework import permissions
from .models import SMS, QrCode
from rest_framework import generics, serializers
from .serializers import SmsSerializer
from rest_framework.response import Response


class SmsCreateView(generics.CreateAPIView):
    queryset = SMS.objects.all()
    serializer_class = SmsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        qr_code = QrCode.objects.create(type_qr_code="sms", user=self.request.user)
        serializer.save(qr=qr_code)
        if serializer.is_valid():
            return Response(
                {
                    "statuts": True,
                    "data": serializer.data,
                    "message": "QR code creer avec succes",
                }
            )
        else:
            return Response(
                {
                    "statuts": False,
                    "data": serializer.errors,
                    "message": "Erreur lors de la creation",
                }
            )


class SmsRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SMS.objects.all()
    serializer_class = SmsSerializer

    def perform_retrieve(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response(
                {
                    "statuts": True,
                    "data": serializer.data,
                    "message": "QR code recuperer avec succes",
                }
            )


class SmsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SMS.objects.all()
    serializer_class = SmsSerializer

    def perform_list(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data})


class SmsUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SMS.objects.all()
    serializer_class = SmsSerializer

    def perform_update(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response(
                {
                    "statuts": True,
                    "data": serializer.data,
                    "message": "QR code mis a jour avec succes",
                }
            )


class SmsDestroyView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SMS.objects.all()
    serializer_class = SmsSerializer

    def perform_destroy(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response(
                {
                    "statuts": True,
                    "data": serializer.data,
                    "message": "QR code supprimer avec succes",
                }
            )
