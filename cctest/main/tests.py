from django.test import TestCase
from .models import People
from .views import HomeView

from django.core.urlresolvers import reverse
# Create your tests here.

class HomeViewTests(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "42 Coffee Cups Test Assignment.")
