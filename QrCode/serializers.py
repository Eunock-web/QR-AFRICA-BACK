from rest_framework import serializers
from .models import Lien, QrCode, Email, Texte, SMS, WIFI, Contact


class LienSerializer(serializers.ModelSerializer):
    qr = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Lien
        fields = ["qr", "lien_url", "description", "logo_url"]


class ContactSerializer(serializers.ModelSerializer):
    qr = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Contact
        fields = [
            "qr",
            "nom",
            "prenom",
            "entreprise",
            "telephone",
            "email",
            "site_web_url",
        ]


class EmailSerializer(serializers.ModelSerializer):
    qr = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Email
        fields = ["qr", "adresse", "sujet", "message"]


class QrSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ["id", "type_qr_code", "user", "created_at", "updated_at"]


class TextSerializer(serializers.ModelSerializer):
    qr = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Texte
        fields = ["qr", "texte"]


class SmsSerializer(serializers.ModelSerializer):
    qr = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SMS
        fields = ["qr", "numero_destinataire", "message"]


class WifiSerializer(serializers.ModelSerializer):
    qr = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = WIFI
        fields = ["qr", "nom_du_reseau", "mot_de_passe", "type_de_chiffrement"]
