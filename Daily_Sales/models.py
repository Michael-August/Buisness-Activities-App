from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

class Payment_Method(models.Model):
    payed_by = models.CharField(max_length=20)

    def __str__(self):
        return self.payed_by

class Daily_Sales(models.Model):
    customer_name = models.CharField(max_length=100)
    item_purchased = models.ManyToManyField(Items)
    quantity = models.IntegerField()
    rate = models.IntegerField()
    total_price = models.IntegerField(default=0)
    date_purchased = models.DateTimeField(auto_now_add=True)
    payment_method = models.ManyToManyField(Payment_Method)
    have_paid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Daily_Sales'

    def __str__(self):
        return self.customer_name

    def save(self):
        self.total_price = self.rate * self.quantity
        super(Daily_Sales, self).save()

