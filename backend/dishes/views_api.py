from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from dishes.models import Dish
from dishes.serializers import DishSerializer


class DishDetailApiViwe(APIView):
    """
    Single Menu object view
    """

    def get(self, request, pk):
        dish = Dish.objects.filter(id=pk).first()
        if not dish:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = DishSerializer(dish, context={'request': request})
        return Response({'results': serializer.data}, status=status.HTTP_200_OK)
