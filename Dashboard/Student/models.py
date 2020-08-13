
from django.db import models
class info(models.Model):
    name = models.CharField(null= False, blank= False, default="", max_length= 50)
    email = models.EmailField(null = False, default="")
    DOB = models.DateField(null = True)
