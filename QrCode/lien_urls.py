from django.urls import path
from .lien_views import LienCreateView, LienRetrieveView, LienListView, LienUpdateView, LienDestroyView

urlpatterns = [
    path("createLien/", LienCreateView.as_view()),
    path("listLien/", LienListView.as_view()),
    path("detailLien/<int:pk>/", LienRetrieveView.as_view()),
    path("updateLien/<int:pk>/", LienUpdateView.as_view()),
    path("deleteLien/<int:pk>/", LienDestroyView.as_view()),
]