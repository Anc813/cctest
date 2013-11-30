from django.test import TestCase
from .models import People, HTTPRequest
from .views import HomeView, HTTPRequestView
from .middleware import StoreRequestsDB

from django.core.urlresolvers import reverse

class HomeViewTests(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "42 Coffee Cups Test Assignment.")

class HTTPRequestViewTests(TestCase):

    def test_HTTPRequestView(self):
        response = self.client.get(reverse('main:requests-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First 10 http requests that are stored by middleware.")

class StoreRequestsDBMiddlewareTests(TestCase):

    def test_HTTPRequest_model_increased(self):
        count = HTTPRequest.objects.all().count()
        response = self.client.get(reverse('main:requests-list'))
        new_count = HTTPRequest.objects.all().count()
        self.assertEqual(count + 1, new_count)