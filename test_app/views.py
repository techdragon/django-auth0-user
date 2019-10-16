from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serialisers import UserSerializer, GroupSerializer, UserSocialAuthSerializer
from rest_framework import permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import APIException
from social_django.models import UserSocialAuth
from test_app.models import Auth0User
from django.http import HttpResponse, JsonResponse


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserDataViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False,
            permission_classes=[permissions.IsAuthenticated],
            url_path='current_user_details', url_name='current-user-details')
    def get_user_data(self, request, *args, **kwargs):
        if request.user:
            # user_social_data = UserSocialAuth.objects.get(user=request.user)
            serializer_context = {
                'request': request,
            }
            serializer = UserSerializer(request.user, context=serializer_context)
            return JsonResponse(serializer.data, safe=True)
        raise APIException('Unable to get User\'s Data')
