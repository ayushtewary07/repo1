from django.db import models
from Student.models import info 
class Batch(models.Model):
    student = models.ForeignKey(info,on_delete=models.PROTECT)
    batch_name = models.CharField(null= False, blank= False, default="", max_length= 100)
    batch_n= models.IntegerField(null= False, blank= False, default= 0, max_length=5)
