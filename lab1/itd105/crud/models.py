from django.db import models

class medicine(models.Model):
    med_name = models.CharField(max_length=100)
    med_brand = models.CharField(max_length=100)
    med_dosage = models.CharField(max_length=100)
    med_expiry = models.DateField()
    med_stock = models.IntegerField()
    med_status = models.CharField(max_length=100)