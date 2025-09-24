from django.urls import path

from .views import(
    CreateLien,
    DetailLien,
    ListLien,
    UpdateLien,
    DestroyLien
)


urlpatterns = [
    path("create/", CreateLien.as_view()),
    path("list/", ListLien.as_view()),
    path("detail/<int:pk>/", DetailLien.as_view()),
    path("update/<int:pk>/", UpdateLien.as_view()),
    path("delete/<int:pk>/", DestroyLien.as_view()),
]