from django.urls import path
from .contact_views import ContactCreateView, ContactRetrieveView, ContactListView, ContactUpdateView, ContactDestroyView

urlpatterns = [
    path("createContact/", ContactCreateView.as_view()),
    path("listContact/", ContactListView.as_view()),
    path("detailContact/<int:pk>/", ContactRetrieveView.as_view()),
    path("updateContact/<int:pk>/", ContactUpdateView.as_view()),
    path("deleteContact/<int:pk>/", ContactDestroyView.as_view()),
]
