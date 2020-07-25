from django.db import models
from menu_categories.models import MenuCategories
from menu_tags.models import MenuTags

class MenuItems(models.Model):
  name = models.CharField(max_length=70, blank=False, null=False)
  description = models.CharField(max_length=256, blank=True, null=True)
  price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
  category = models.ForeignKey(MenuCategories, on_delete=models.CASCADE, blank=False, null=False)
  tags = models.ManyToManyField(MenuTags, blank=True)

  def __str__(self):
    return self.name