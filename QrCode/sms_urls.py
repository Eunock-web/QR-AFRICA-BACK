from django.urls import path
from .sms_views import SmsCreateView, SmsRetrieveView, SmsListView, SmsUpdateView, SmsDestroyView

urlpatterns = [
    path("createSms/", SmsCreateView.as_view()),
    path("listSms/", SmsListView.as_view()),
    path("detailSms/<int:pk>/", SmsRetrieveView.as_view()),
    path("updateSms/<int:pk>/", SmsUpdateView.as_view()),
    path("deleteSms/<int:pk>/", SmsDestroyView.as_view()),
]
