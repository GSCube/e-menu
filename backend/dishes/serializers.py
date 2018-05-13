from rest_framework.serializers import HyperlinkedModelSerializer, \
    HyperlinkedIdentityField, ModelSerializer

from dishes.models import Dish


class DishSerializer(ModelSerializer):
    """
    Dish model's serializer
    """
    menu = HyperlinkedIdentityField(view_name='menu:api-menu-details', source='menu')

    class Meta:
        model = Dish
        fields = '__all__'
