from leader.models import Leader
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User
from .serializers import LeaderSerializer, UserSerializer, LeaderSerializerPublic
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class LeaderSubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer


class LeaderAuthorSubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions, AuthorOrReadOnly]
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer


class LeaderPublicViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Leader.objects.filter(leader_status='P')
    serializer_class = LeaderSerializerPublic


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['GET', 'PUT', 'HEAD']
    permission_classes = [permissions.AllowAny, AuthorOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LeaderList(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'leader_list.html'

    def get(self, request):
        if Leader.objects.all() is not None:
            queryset = Leader.objects.filter(leader_status='P')
            return Response({'leaders': queryset})


class LeaderListSus(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'leader_list_s.html'

    def get(self, request):
        queryset = Leader.objects.all()
        return Response({'leaders': queryset})
