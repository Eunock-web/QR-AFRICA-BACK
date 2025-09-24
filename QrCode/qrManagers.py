from .models import QrCode
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response

'''
    Classe pour gerer les statistiques concernant le nombre de QRcode creer 
'''
class QrcodeStatsView(APIView):
    def getTotal(self, request):
        # Total
        total = QrCode.objects.count()
        return Response({ 'statuts':True , "total": total})


    def get_type(APIView):
        # Groupé par type
        by_type = QrCode.objects.values("type").annotate(count=Count("id"))

        return Response({"total": by_type, "statuts": True})
