from pyexpat import model
from unicodedata import name
from django.db import models



class Item(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.name} {self.quantity}"
    


