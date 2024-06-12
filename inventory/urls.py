from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, SupplierViewSet
from . import views


router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]