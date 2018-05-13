from django.db import models
from django.utils.translation import ugettext as _


class BaseMenuModel(models.Model):
    """
    Abstract Model for Menu Cards and Dish
    """
    title = models.CharField(verbose_name=_('name'), max_length=120, unique=True, blank=False)
    description = models.TextField(verbose_name=_('description'), max_length=600)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modification date'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
