from django.test import TestCase
from django.urls import reverse

class MenuViewTest(TestCase):
    def test_menu_view(self):
        response = self.client.get('http://localhost:8000/restaurant/')
        self.assertEqual(response.status_code, 200)