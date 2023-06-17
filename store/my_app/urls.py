from django.urls import include, path
from rest_framework import routers
from my_app.views import ProductViewSet

router = routers.DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 