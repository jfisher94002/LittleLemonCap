from django.test import TestCase

from ..models import MenuItem


class MenuItemTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Test Item", price=10.00, inventory=5)

    def test_menu_item_creation(self):
        item = MenuItem.objects.get(title="Test Item")
        self.assertEqual(item.price, 10.00)
        self.assertEqual(item.inventory, 5)
