from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
