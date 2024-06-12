from rest_framework import viewsets
from .models import Item, Supplier
from .serializers import ItemSerializer, ItemDetailSerializer, SupplierSerializer, SupplierDetailSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'create', 'update', 'partial_update']:
            return ItemSerializer
        return ItemDetailSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'create', 'update', 'partial_update']:
            return SupplierSerializer
        return SupplierDetailSerializer

