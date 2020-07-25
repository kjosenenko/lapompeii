from django.db import models

class Schedule(models.Model):
  location = models.CharField(max_length=35, blank=False, null=False)
  description = models.CharField(max_length=256, blank=False, null=True)
  start_date = models.DateField(blank=False, null=True)
  start_time = models.TimeField(blank=False, null=True)
  end_date = models.DateField(blank=False, null=True)
  end_time = models.TimeField(blank=False, null=True)

  def __str__(self):
    return self.location