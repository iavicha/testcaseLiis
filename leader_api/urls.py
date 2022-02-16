from django.urls import path, include
from rest_framework import routers
from .views import LeaderPublicViewSet, LeaderSubscriptionViewSet, UserViewSet, LeaderList, LeaderListSus, \
    LeaderAuthorSubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'Public', LeaderPublicViewSet, basename='public')
router.register(r'Subscription', LeaderSubscriptionViewSet, basename='subscription')
router.register(r'user', UserViewSet, basename='User')
router.register(r'author', LeaderAuthorSubscriptionViewSet, basename='Author')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', LeaderList.as_view()),
    # path('registred/', LeaderListSus.as_view()),
]
