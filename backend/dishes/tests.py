from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from dishes.models import Dish
from dishes.views_api import DishDetailApiViwe
from menu.models import Menu


class DishModelTest(TestCase):
    """
    Dish Model test
    """

    def test_string_representation(self):
        menu = Dish(title='Danie testowe')
        self.assertEqual(str(menu), menu.title)

    def test_verbose_name(self):
        self.assertEqual(str(Dish._meta.verbose_name), 'dishes')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Dish._meta.verbose_name_plural), 'dishes')


class TestDishDetailApiView(APITestCase):

    def test_dish_detail_view(self):
        menu = Menu.objects.create(title='Test Dish')
        dish = Dish.objects.create(title='Test 2', price=2.20, menu=menu)
        factory = APIRequestFactory(pk=dish.pk)
        view = DishDetailApiViwe.as_view()
        request = factory.get(reverse('dishes:api-dish-details', args=(dish.pk,)))
        response = view(request, pk=dish.id)
        response_data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response_data)
        self.assertEqual(dish.id, response_data.get('results').get('id'))
