from django.urls import path, include
from rest_framework import routers
from .views import LeaderPublicViewSet, LeaderSubscriptionViewSet, UserViewSet, LeaderAuthorSubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'public', LeaderPublicViewSet, basename='public')
router.register(r'subscription', LeaderSubscriptionViewSet, basename='subscription')
router.register(r'user', UserViewSet, basename='User')
router.register(r'author', LeaderAuthorSubscriptionViewSet, basename='Author')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

