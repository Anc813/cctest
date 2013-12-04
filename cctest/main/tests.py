from django.test import TestCase
from .models import People, HTTPRequest, SignalProcessor
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

    def test_requests_added_to_db(self):
        '''
        Test requests are really added to database
        '''
        count = HTTPRequest.objects.all().count()
        response = self.client.get(reverse('main:requests-list'))
        new_count = HTTPRequest.objects.all().count()
        self.assertEqual(count + 1, new_count)

        item =  HTTPRequest.objects.all().order_by('-pk')[:1][0]
        self.assertEqual(item.path, reverse('main:requests-list'))
        self.assertEqual(item.method, 'GET')


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

class EditLinkTests(TestCase):

    def test_edit_people_item(self):
        from django.template import Template, Context

        item = People.objects.all()[:1][0]
        t = Template('{% load edit_link %}{% edit_link object %}')
        c = Context({'object' : item })
        self.assertEqual(t.render(c), '/admin/main/people/%d/' % item.pk)

    def test_raises_other_object(self):
        from django.template import Template, Context
        t = Template('{% load edit_link %}{% edit_link object %}')
        c = Context({'object' : self })
        self.assertRaises(AttributeError, lambda: t.render(c) )

class ModelsInfoCommandTests(TestCase):

    def test_command(self):
        '''
        Test models_info command
        '''
        from django.core.management import call_command
        from StringIO import StringIO

        content = StringIO()
        call_command("models_info", stdout=content)
        content.seek(0)
        s =  content.read()
        self.assertIn('model main.people has', s)

class SignalProcessorTests(TestCase):

    def getPeopleItem(self):
        return People(name = '1', surname = '1', birth_date = '2012-11-11', bio = '1',
                       email = 'admin@example.com', other_contacts = '1')

    def test_create(self):
        '''
        Test Signal Processor that objects are really added when created
        '''
        item = self.getPeopleItem()

        # save
        count = SignalProcessor.objects.all().count()
        item.save()
        new_count = SignalProcessor.objects.all().count()
        self.assertEqual(count + 1, new_count)

    def test_update(self):
        '''
        Test Signal Processor that objects are really added when updated
        '''
        item = self.getPeopleItem()

        item.save()
        item.name = '2'

        count = SignalProcessor.objects.all().count()
        item.save()
        new_count = SignalProcessor.objects.all().count()
        self.assertEqual(count + 1, new_count)

    def test_delete(self):
        '''
        Test Signal Processor that objects are really added when deleted
        '''
        item = self.getPeopleItem()

        item.save()

        count = SignalProcessor.objects.all().count()
        item.delete()
        new_count = SignalProcessor.objects.all().count()
        self.assertEqual(count + 1, new_count)

class HTTPRequestPriorityFieldTest(TestCase):

    def test_bigger_priority_is_first(self):
        '''
        Test that records with bigger priority comes first
        make two request, modify prior of them, ensure that request with bigger priority comes first
        '''
        response = self.client.get(reverse('main:home'))
        count = HTTPRequest.objects.all().count()
        record = HTTPRequest.objects.all()[:1][0]
        record.priority = 1
        record.save()
        pk = record.pk
        response = self.client.get(reverse('main:home'))
        self.assertEqual(HTTPRequest.objects.all().count(), count + 1)
        record = HTTPRequest.objects.all()[:1][0]
        self.assertEqual(pk, record.pk)
