from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameRankViewSet

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix, 두 번째 인자는 ViewSet
router.register('gamerank', GameRankViewSet )

urlpatterns = [
    path('', include(router.urls)),
]