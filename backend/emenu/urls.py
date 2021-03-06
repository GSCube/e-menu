"""emenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from emenu.views import ReactAppView
from emenu.views_appi import MenuAndDishesListApiView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='menu/home.html'), name='home'),
    path('', ReactAppView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/get_menues_and_dishes/', MenuAndDishesListApiView.as_view(), name='get_all_data'),
    path('api/menu/', include('menu.urls', namespace='menu')),
    path('api/dish/', include('dishes.urls', namespace='dishes')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
