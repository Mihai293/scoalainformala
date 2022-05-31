from django.db import models


coin_choices = (('btc', 'btc'), ('eth', 'eth'))


class Wallet(models.Model):
    coin_number = models.CharField(max_length=100)
    coin_type = models.CharField(max_length=3, choices=coin_choices)

    def __str__(self):
        return f' {self.coin_number}, {self.coin_type}'
