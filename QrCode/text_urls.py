from django.urls import path
from .text_views import TextCreateView, TextRetrieveView, TextListView, TextUpdateView, TextDestroyView

urlpatterns = [
    path("createText/", TextCreateView.as_view()),
    path("listText/", TextListView.as_view()),
    path("detailText/<int:pk>/", TextRetrieveView.as_view()),
    path("updateText/<int:pk>/", TextUpdateView.as_view()),
    path("deleteText/<int:pk>/", TextDestroyView.as_view()),
]
