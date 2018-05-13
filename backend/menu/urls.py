from django.urls import path

from menu.views_api import MenuListApiView, MenuDetailApiViwe

app_name = 'menu'

urlpatterns = [
    path('list/', MenuListApiView.as_view(), name='api-menu-list'),
    path('<int:pk>/', MenuDetailApiViwe.as_view(), name='api-menu-details')
]
