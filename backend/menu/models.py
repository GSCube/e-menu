from django.urls import reverse
from django.utils.translation import ugettext as _

from emenu.base_models import BaseMenuModel


class Menu(BaseMenuModel):
    """
    Menu Card
    """

    class Meta:
        verbose_name = _('menu card')
        verbose_name_plural = _('menu cards')

    # def get_absolute_url(self):
    #     return reverse('menu:api-menu-details', self.id)
