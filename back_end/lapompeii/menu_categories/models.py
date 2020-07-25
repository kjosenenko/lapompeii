from django.db import models

class MenuCategories(models.Model):
  name = models.CharField(max_length=70, blank=False, null=False)
  description = models.CharField(max_length=256, blank=True, null=True)
  price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


  def __str__(self):
    return self.name
