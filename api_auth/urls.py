from django.urls import path
from .views import AllUsers, RegisterUserView, LoginView

urlpatterns = [
    path('users/register', RegisterUserView.as_view()),
    path('users/login', LoginView.as_view()),
    path('users/lists', AllUsers.as_view())
]