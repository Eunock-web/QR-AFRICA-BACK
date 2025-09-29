from rest_framework import permissions
from .models import Email, QrCode
from rest_framework import generics, serializers
from .serializers import EmailSerializer
from rest_framework.response import Response


class EmailCreateView(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        qr_code = QrCode.objects.create(type_qr_code="email", user=self.request.user)
        serializer.save(qr=qr_code)

        return Response({
            "statuts": True,
            "data": serializer.data,
            "message": "QR code créé avec succès"
        })



class EmailRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

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


class EmailListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def perform_list(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data})


class EmailUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

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


class EmailDestroyView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

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
