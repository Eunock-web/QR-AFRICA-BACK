from rest_framework import serializers
from .models import Lien, QrCode
# from .models import Email
# from .models import Text
# from .models import SMS
# from .models import WIFI
# from .models import Contact


"""
    -LienSerializer: Serializer pour la gestion des Liens(données acceptées et type de donnée)
"""

class LienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lien
        fields = ['lien_url','description', 'logo_url']
        
        
class QrSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ['type_qr_code', 'user_id']