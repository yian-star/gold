from django.db import models


# Create your models here.
class Customer(models.Model):
    nature = models.CharField(max_length=100)
    company_name = models.CharField(max_length=20)
    tax_rate = models.FloatField(default=0)
    regist_time = models.DateTimeField(auto_now_add=True)


