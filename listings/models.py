from django.contrib.auth.models import User
from django.db import models

from starships.models import Starship


class Listing(models.Model):
    LISTING_STATUSES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    
    created = models.DateTimeField('Created at', auto_created=True)
    updated = models.DateTimeField('Updated at', auto_now=True)

    status = models.CharField(
        'Status',
        choices=LISTING_STATUSES,
        max_length=8,
        default='active',
        blank=False,
        null=False
    )
    seller = models.ForeignKey(
        User,
        verbose_name='Seller',
        on_delete=models.CASCADE,
        null=False
    )
    starship = models.ForeignKey(
        Starship,
        verbose_name='Starship',
        on_delete=models.CASCADE,
        null=False
    )
    sale_price = models.IntegerField('Asking Price', blank=False, null=False)
    sold = models.BooleanField('Sold', default=False, null=False)

    def __str__(self):
        return "{}'s {}".format(self.seller.first_name, self.starship)
