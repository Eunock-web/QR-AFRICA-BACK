from pyexpat import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

'''
    Les Models :
        -Lien:Pour la table permettant d'enregistrer les liens qu'on aura a transformer en QR code avec les autres champs y compris
        
        -Email: Pour la table Email permettant d'enregistrer le message a envoyer par Email qui sera transcrit en QR code
        
        -Texte: Pour la table Texte permettant de convertir un messages(Texte) sous forme de QR code
        
        -SMS: La table SMS qui se charge de la l'enregistrement des informations concernant le message qu'on veut envoyer a une personne par sms pour la conversion en Qr code
        
        -WIFI: La table qui se charge de l'enregistrement des infos sur un reseau wifi pour permettre la connexion automatique a un wifi apres la generation du Qr code
        
        -Contact Vcard:
'''

class  QrCode(models.Model):  # Définition des choix comme tuple de tuples
    TYPE_LIEN = "lien"
    TYPE_TEXTE = "texte"
    TYPE_EMAIL = "email"
    TYPE_WIFI = "wifi"
    TYPE_SMS = "sms"
    TYPE_CONTACT = "contact"
    
    TYPE_QR_CODE = [
        (TYPE_TEXTE , "texte")
        (TYPE_EMAIL , "email")
        (TYPE_WIFI , "wifi")
        (TYPE_LIEN , "lien")
        (TYPE_SMS , "sms")
        (TYPE_CONTACT , "contact")
    ]
    type_qr_code = models.CharField(max_length = 100, choices = TYPE_QR_CODE, default = TYPE_TEXTE)
    user_id = models.ForeignKey('auth.User', on_delete = models.CASCADE, related_name = 'qrcodes')
 


class Lien(models.Model):
    lien_url = models.URLField(max_lenght=255, help_text="Entrez une URL complète avec http:// ou https://")
    description = models.CharField(max_lenght=255, null=True, blanck=True)
    logo_url = models.CharField(max_lenght=255, null=True, blanck=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Email(models.Model):
    adresse = models.EmailField()
    sujet = models.CharField(max_lenght = 255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Texte(models.Model):
    texte = models.TextField()
    
    
class SMS(models.Model):
    numero_destinataire = models.CharField(max_length = 100)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class WIFI(models.Model):
    nom_du_reseau = models.CharField(max_length = 100)
    mot_de_passe = models.CharField(max_length = 255)
    type_de_chiffrement = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    entreprise = models.CharField(max_length = 150)
    telephone = models.CharField(max_length = 100)
    email = models.EmailField()
    site_web_url = models.URLField(max_length=100, null=True, blanck=True, help_text="Entrez une URL complète avec http:// ou https://")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
