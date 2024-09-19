from django.urls import path,include
from rest_framework import routers

from services.views import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'services',ServiceViewSet)

urlpatterns = [path('', include(router.urls))]