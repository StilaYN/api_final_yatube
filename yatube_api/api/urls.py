from django.urls import include, path
from .views import GroupViewSet, PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)



urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
