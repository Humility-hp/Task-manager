from django.db import models
# from django.contrib.auth.models import user
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
def contactVal(contact):
 validate = re.findall("^080.{8}$|^081.{8}$|^090.{8}$|^070.{8}$", contact)
 if not validate:
  raise ValidationError(("%(contact)s must be a nigerian number"), params={"contact":contact})
 

class pendingUsers(models.Model):
  first_name = models.CharField("username", max_length=20)
  last_name = models.CharField(max_length=20)
  contact_info = models.CharField(max_length=11, unique=True, validators=[contactVal])
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15, unique=True)

  def __str__(self):
    return f"{self.first_name}" 

class assignment(models.Model):
  created_by = models.ForeignKey(pendingUsers, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  essay = models.CharField(max_length=200)

  def __str__(self):
    return self.created