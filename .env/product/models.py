from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    product_category=models.CharField(max_length=200)
    created_date=models.DateTimeField()
    available_items=models.IntegerField(blank=True,null=True)
    class Meta:
        ordering=['name']

    def __str__(self) :
        return "{} {}".format(self.name,self.product_category)