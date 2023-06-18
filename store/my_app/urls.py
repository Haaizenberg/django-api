from django.urls import include, path
from rest_framework import routers
from my_app.views import CarViewSet

router = routers.DefaultRouter()
router.register('', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 