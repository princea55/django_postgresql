from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    profile = models.TextField()
    def __str__(self):
        return self.name

class Stock(models.Model):
    idx = models.IntegerField()
    date = models.DateField()
    symbol = models.CharField(max_length=50)
    opens = models.FloatField()
    close = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.symbol
