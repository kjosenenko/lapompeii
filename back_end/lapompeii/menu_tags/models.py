from django.db import models

class MenuTags(models.Model):
  name = models.CharField(max_length=70, blank=False, null=False)


  def __str__(self):
    return self.name
