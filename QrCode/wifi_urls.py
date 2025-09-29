from django.urls import path
from .wifi_views import WifiCreateView, WifiRetrieveView, WifiListView, WifiUpdateView, WifiDestroyView

urlpatterns = [
    path("createWifi/", WifiCreateView.as_view()),
    path("listWifi/", WifiListView.as_view()),
    path("detailWifi/<int:pk>/", WifiRetrieveView.as_view()),
    path("updateWifi/<int:pk>/", WifiUpdateView.as_view()),
    path("deleteWifi/<int:pk>/", WifiDestroyView.as_view()),
]
