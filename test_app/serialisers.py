from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from social_django.models import UserSocialAuth
from rest_framework import serializers


User = get_user_model()


class UserSocialAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocialAuth
        fields = ('provider', 'uid', 'extra_data', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    social_auth = UserSocialAuthSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'username',
            'groups',
            # 'auth0_data',
            'id_token_payload',
            'access_token_payload',
            'refresh_token_payload',
            'social_auth',
            # 'url',
            # 'name'
            # 'email',
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



