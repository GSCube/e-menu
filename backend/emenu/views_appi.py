from emenu.base_views_api import ListApiView
from menu.models import Menu
from menu.serializers import MenuAndDishSerializer


class MenuAndDishesListApiView(ListApiView):
    """
    Widok generyczny API zwracający listę obiektów, obsługiwana metoda GET
    """

    serializer_class = MenuAndDishSerializer

    def get_queryset(self):
        # not empty menu card
        return Menu.objects.prefetch_related('dishes').exclude(dishes__isnull=True).order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

