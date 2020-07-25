from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Emails(models.Model):
  email = models.EmailField(max_length = 254, blank=False, null=False)
  name = models.CharField(max_length=70, blank=False, null=False)
  comment = models.CharField(max_length=256, blank=True, null=True)
  phone = PhoneNumberField(blank=True, null=True)


  def __str__(self):
    return self.name
