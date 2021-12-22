from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Apprentice(models.Model):
    apprentice_name = models.CharField(max_length=70)

    def __str__(self):
        return self.apprentice_name

class CollectedItems(models.Model):
    item_collected = models.CharField(max_length=70)
    quantity = models.IntegerField()
    rate = models.IntegerField()
    total_price = models.IntegerField(default=0)
    collected_from = models.CharField(max_length=70)
    collected_by = models.ForeignKey(Apprentice, on_delete=CASCADE)
    date_collected = models.DateTimeField(auto_now_add=True)
    date_paid = models.DateTimeField(auto_now_add=True)
    have_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.item_collected

    def save(self):
        self.total_price = self.quantity * self.rate
        super(CollectedItems, self).save()
