from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse


from emenu.base_models import BaseMenuModel


class Dish(BaseMenuModel):
    """
    Dish
    """
    price = models.DecimalField(verbose_name=_('price'), max_digits=6, decimal_places=2)
    cook_time = models.CharField(verbose_name=_('cook time [h]'), max_length=3)
    is_vegetarian = models.BooleanField(verbose_name=_('vegetarian dishes?'), default=False, null=False)
    menu = models.ForeignKey('menu.Menu', verbose_name=_('menu cards'), blank=True, null=True,
                             related_name='dishes', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('image'), upload_to='dishes/')

    class Meta:
        verbose_name = _('dishes')
        verbose_name_plural = _('dishes')

    # def get_absolute_url(self):
    #     return reverse('dishes:api-dish-details', self.id)
