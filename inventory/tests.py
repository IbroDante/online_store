from django.test import TestCase
from .models import Item, Supplier


# Create your tests here.
class InventoryTests(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_information="Contact Info")
        self.item = Item.objects.create(name="Test Item", description="Item Description", price=20)
        self.item.suppliers.add(self.supplier)

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertIn(self.supplier, self.item.suppliers.all())

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.name, "Test Supplier")
        self.assertIn(self.item, self.supplier.items.all())
