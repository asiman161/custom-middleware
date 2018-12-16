from django.urls import path

from .views import PollView

urlpatterns = [
    path(r'', PollView.as_view()),
    path('<str:id>/', PollView.as_view()),
]
