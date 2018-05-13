from django.urls import path

from dishes.views_api import DishDetailApiViwe, DishesListApiView

app_name = 'dishes'

urlpatterns = [
    path('list/<int:pk>', DishesListApiView.as_view(), name='api-dishes-list'),
    path('<int:pk>/', DishDetailApiViwe.as_view(), name='api-dish-details')
]
