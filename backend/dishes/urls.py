from django.urls import path

from dishes.views_api import DishDetailApiViwe

app_name = 'dishes'

urlpatterns = [
    path('<int:pk>/', DishDetailApiViwe.as_view(), name='api-dish-details')
]
