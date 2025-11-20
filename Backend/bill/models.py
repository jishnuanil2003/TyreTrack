from django.db import models

# Create your models here.
class BillModel(models.Model):
    name = models.CharField(max_length=55)
    service = models.CharField(max_length=55)
    date = models.DateField(default='10/11/2025')
    time = models.TimeField(default="00:00 AM")
    price = models.IntegerField()
    payment = models.CharField(max_length=20)
    tyre_size = models.CharField(max_length=55,null=True,blank=True)
    tyre_name = models.CharField(max_length=55,null=True,blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.service}"