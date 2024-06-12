from rest_framework import serializers
from .models import Item, Supplier


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added'] 

class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_information', 'items'] 

class SupplierDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_information', 'items'] 

class ItemDetailSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers'] 
