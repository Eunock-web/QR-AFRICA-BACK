from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)  # Date de maj

    class Meta:
        abstract = True


class QrCode(BaseModel):
    TYPE_LIEN = "lien"
    TYPE_TEXTE = "texte"
    TYPE_EMAIL = "email"
    TYPE_WIFI = "wifi"
    TYPE_SMS = "sms"
    TYPE_CONTACT = "contact"

    TYPE_QR_CODE = [
        (TYPE_TEXTE, "text"),
        (TYPE_EMAIL, "email"),
        (TYPE_WIFI, "wifi"),
        (TYPE_LIEN, "lien"),
        (TYPE_SMS, "sms"),
        (TYPE_CONTACT, "contact"),
    ]

    type_qr_code = models.CharField(
        max_length=100, choices=TYPE_QR_CODE, default=TYPE_TEXTE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Lien(BaseModel):
    qr = models.OneToOneField(QrCode, on_delete=models.CASCADE)
    lien_url = models.URLField(
        max_length=255, help_text="Entrez une URL complète avec http:// ou https://"
    )
    description = models.CharField(max_length=255, null=True, blank=True)
    logo_url = models.CharField(max_length=255, null=True, blank=True)


class Email(BaseModel):
    qr = models.OneToOneField(QrCode, on_delete=models.CASCADE, related_name="email")
    adresse = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()


class Texte(BaseModel):
    qr = models.OneToOneField(QrCode, on_delete=models.CASCADE, related_name="texte")
    texte = models.TextField()


class SMS(BaseModel):
    qr = models.OneToOneField(QrCode, on_delete=models.CASCADE, related_name="sms")
    numero_destinataire = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


class WIFI(BaseModel):
    qr = models.OneToOneField(QrCode, on_delete=models.CASCADE, related_name="wifi")
    nom_du_reseau = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    type_de_chiffrement = models.CharField(max_length=20)


class Contact(BaseModel):
    qr = models.OneToOneField(QrCode, on_delete=models.CASCADE, related_name="contact")
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=150)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    site_web_url = models.URLField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Entrez une URL complète avec http:// ou https://",
    )
