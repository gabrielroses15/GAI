from django.urls import path
from .views import PerguntaListView, PerguntaDetailView

urlpatterns = [
    path('perguntas/', PerguntaListView.as_view(), name='pergunta-list'),
    path('perguntas/<int:pk>/', PerguntaDetailView.as_view(), name='pergunta-detail'),
]
