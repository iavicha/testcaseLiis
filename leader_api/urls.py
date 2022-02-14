from django.urls import path, include
from rest_framework import routers
from .views import LeaderPublicViewSet, LeaderSubscriptionViewSet, UserViewSet, LeaderList, LeaderListSus, \
    LeaderAuthorSubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'Public', LeaderPublicViewSet, 'public')
router.register(r'Subscription', LeaderSubscriptionViewSet, 'subscription')
router.register(r'create_user', UserViewSet, 'create_user')
router.register(r'author', LeaderAuthorSubscriptionViewSet, 'Author')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', LeaderList.as_view()),
    path('registred/', LeaderListSus.as_view()),
]
