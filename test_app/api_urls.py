from rest_framework import routers
from test_app.views import UserViewSet
from test_app.views import GroupViewSet
from test_app.views import UserDataViewSet


api_v1 = routers.DefaultRouter()
api_v1.register(r'users', UserViewSet)
api_v1.register(r'groups', GroupViewSet)
api_v1.register(r'user_data', UserDataViewSet, basename='user-data')

