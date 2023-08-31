from django.db import models

# Create your models here.

class Services(models.Model):
    # id:int
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    spc = models.BooleanField(default=False)
    price = models.IntegerField()

