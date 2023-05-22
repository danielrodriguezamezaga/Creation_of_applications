from email.policy import default
from django.db import models

class irisModel(models.Model):
    sepal_length = models.FloatField(blank=True, default=0)
    sepal_width = models.FloatField(blank=True, default=0)
    petal_length = models.FloatField(blank=True, default=0)
    petal_width = models.FloatField(blank=True, default=0)
    species = models.CharField(max_length=30, blank=True, default="")