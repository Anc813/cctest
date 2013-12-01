from django.test import TestCase
from .models import People, HTTPRequest
from .views import HomeView, HTTPRequestView, HomeEditView
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

class SettingsContextProcessorTests(TestCase):

    def test_settings(self):
        from django.template import RequestContext
        from django.conf import settings as django_settings

        response = self.client.get(reverse('main:home'))
        c = RequestContext(response)
        self.assertTrue('settings' in c)
        self.assertEquals(c['settings'], django_settings)

class PeopleMethodTests(TestCase):

    def test_get_absolute_url(self):
        """
        contains at least one element, loaded from fixtures
        get_absolute_url is accesible
        """
        item = People.objects.all()[:1]
        self.assertTrue(item)
        response = self.client.get(item[0].get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "42 Coffee Cups Test Assignment.")

class HomeEditViewTests(TestCase):

    def test_unathorized_access_is_forbidden(self):
        """
        editing is forbidden withouth login
        """
        item = People.objects.all()[:1][0]
        response = self.client.get(reverse("main:edit", args=[item.pk]))
        self.assertEqual(response.status_code, 302)

    def test_authorized_access_is_granted(self):
        '''
        editing with admin/admin is granted
        '''
        item = People.objects.all()[:1][0]
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse("main:edit", args=[item.pk]))
        self.assertEqual(response.status_code, 200)

    def test_form_is_failed(self):
        item = People.objects.all()[:1][0]
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse("main:edit", args=[item.pk]), {'name':'name'})
        self.assertFormError(response, 'form', 'birth_date', 'This field is required.')

    def test_form_is_success(self):
        item = People.objects.all()[:1][0]
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse("main:edit", args=[item.pk]),
                                    {'name':'1', 'surname':'1', 'birth_date':'2012-11-11',
                                     'bio':'1', 'email' :'admin@example.com', 'other_contacts' : '1'})
        #print response.context['form'].errors
        self.assertEqual(response.status_code, 302)

    def test_ajax_form_is_success(self):
        item = People.objects.all()[:1][0]
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse("main:edit", args=[item.pk]),
                                    {'name':'1', 'surname':'1', 'birth_date':'2012-11-11',
                                     'bio':'1', 'email' :'admin@example.com', 'other_contacts' : '1'},
                                     HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        #print response.context['form'].errors
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Changes have been saved')