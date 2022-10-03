from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_price(self):
        return f'{self.price / 100:0.2f}'
