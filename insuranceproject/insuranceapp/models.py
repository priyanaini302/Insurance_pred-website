from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class insurance(models.Model):
    age=models.IntegerField()
    sex=models.IntegerField()
    bmi=models.FloatField()
    children=models.IntegerField()
    smoker=models.IntegerField()