from django.db import models

# Create your models here.
class InventoryModel(models.Model):
    item_name = models.CharField(max_length=100)
    item_size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    serial = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=25,blank=True, null=True)

    def save(self,*args, **kwargs):
        if self.quantity <= 0:
            self.status = 'Out of Stock'
        elif self.quantity == 1:
            self.status = 'Low Stock'
        else:
            self.status = 'In Stock'
        super().save(*args, **kwargs)      