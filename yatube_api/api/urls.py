from django.urls import include, path
from .views import GroupViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)



urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
