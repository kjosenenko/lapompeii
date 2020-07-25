from django.db import models

class TextAreas(models.Model):
  title = models.CharField(max_length=70, blank=False, null=False)
  textArea = models.CharField(max_length=20000, blank=False, null=True)

  def __str__(self):
    return self.title
