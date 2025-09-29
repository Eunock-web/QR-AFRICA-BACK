from rest_framework import permissions
from .models import Texte, QrCode
from rest_framework import generics, serializers
from .serializers import TextSerializer
from rest_framework.response import Response


class TextCreateView(generics.CreateAPIView):
    queryset = Texte.objects.all()
    serializer_class = TextSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        qr_code = QrCode.objects.create(type_qr_code="texte", user=self.request.user)
        serializer.save(qr=qr_code)

        return Response(
            {
                "statuts": True,
                "data": serializer.data,
                "message": "QR code créé avec succès",
            }
        )


class TextRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Texte.objects.all()
    serializer_class = TextSerializer

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


class TextListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Texte.objects.all()
    serializer_class = TextSerializer

    def perform_list(self, serializer):
        qr_code = QrCode.objects.get(id=self.kwargs["pk"])
        serializer.save(qr=qr_code)
        if qr_code.user != self.request.user:
            raise serializers.ValidationError("Vous n'avez pas accès à ce QR code")
        else:
            return Response({"statuts": True, "data": serializer.data})


class TextUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Texte.objects.all()
    serializer_class = TextSerializer

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


class TextDestroyView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Texte.objects.all()
    serializer_class = TextSerializer

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
