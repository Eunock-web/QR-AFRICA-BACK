from django.urls import path
from .email_views import EmailCreateView, EmailRetrieveView, EmailListView, EmailUpdateView, EmailDestroyView

urlpatterns = [
    path("email/create", EmailCreateView.as_view(), name="email_create"),
    path("email/retrieve/<int:pk>", EmailRetrieveView.as_view(), name="email_retrieve"),
    path("email/list", EmailListView.as_view(), name="email_list"),
    path("email/update/<int:pk>", EmailUpdateView.as_view(), name="email_update"),
    path("email/destroy/<int:pk>", EmailDestroyView.as_view(), name="email_destroy"),
]