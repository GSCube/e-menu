from emenu.base_views_api import ListApiView
from emenu.base_paginators import BasePaginator
from menu.models import Menu
from menu.serializers import MenuSerializer, MenuSerializerWithDish
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MenuListApiView(ListApiView):
    """
    Widok generyczny API zwracający listę obiektów, obsługiwana metoda GET
    """

    serializer_class = MenuSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        # not empty menu card
        return Menu.objects.exclude(dishes__isnull=True).order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MenuDetailApiViwe(APIView):
    """
    Single Menu object view
    """

    def get(self, request, pk):
        menu_object = Menu.objects.filter(id=pk).first()
        if not menu_object:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = MenuSerializerWithDish(menu_object, context={'request': request})
        return Response({'results': serializer.data}, status=status.HTTP_200_OK)
