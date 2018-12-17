from django.urls import path

from .views import PollView

urlpatterns = [
    path(r'', PollView.as_view(), name='polls'),
    path('<str:pk>/', PollView.as_view(), name='polls'),
]
