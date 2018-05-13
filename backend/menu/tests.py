from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory

from menu.models import Menu
from menu.serializers import MenuSerializer
from menu.views_api import MenuListApiView, MenuDetailApiViwe


class MenuModelTest(TestCase):
    """
    Menu Card Model test
    """

    def test_string_representation(self):
        menu = Menu(title='Testowe Menu')
        self.assertEqual(str(menu), menu.title)

    def test_verbose_name(self):
        self.assertEqual(str(Menu._meta.verbose_name), 'menu card')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Menu._meta.verbose_name_plural), 'menu cards')


class TestMenuApiView(APITestCase):

    def setUp(self):
        Menu.objects.create(title='Test')
        Menu.objects.create(title='Test 2')

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_menu_list_viwe(self):
        factory = APIRequestFactory()
        view = MenuListApiView.as_view()
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)
        url = reverse('menu:api-menu-list')
        request = factory.get(url)
        response = view(request)
        response_result = dict(response.data.items()).get('results')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response_result, serializer.data)  # Empty List, Menu without dish

    def test_menu_detail_view(self):
        menu = Menu.objects.create(title='Test Dish')
        factory = APIRequestFactory(pk=menu.pk)
        view = MenuDetailApiViwe.as_view()
        request = factory.get(reverse('menu:api-menu-details', args=(menu.pk,)))
        response = view(request, pk=menu.id)
        response_data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response_data)
        self.assertEqual(menu.id, response_data.get('results').get('id'))
