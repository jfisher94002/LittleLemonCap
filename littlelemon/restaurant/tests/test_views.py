from django.test import TestCase

from ..models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Test Item", price=10.00, inventory=5)

    def test_menu_item_view(self):
        MenuItem.objects.all()
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        print(response.content)
