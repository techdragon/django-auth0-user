from rest_framework import routers
from .views import UserViewSet
from .views import GroupViewSet


api_v1 = routers.DefaultRouter()
api_v1.register(r'users', UserViewSet)
api_v1.register(r'groups', GroupViewSet)


