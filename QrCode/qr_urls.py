from django.urls import path
from .qr_views import AllQrCodesView, QrCodeByTypeListView

urlpatterns = [
    path('all_qrcodes/', AllQrCodesView.as_view()),
    path('qrcodes_by_type/<str:type>/', QrCodeByTypeListView.as_view()),
]
