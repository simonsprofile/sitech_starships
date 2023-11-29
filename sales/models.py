from django.contrib.auth.models import User
from django.db import models

from listings.models import Listing


class Sale(models.Model):
    SALE_STATUSES = (
        ('pending', 'Pending'),
        ('complete', 'Complete'),
    )
    
    created = models.DateTimeField('Created at', auto_created=True)
    updated = models.DateTimeField('Updated at', auto_now=True)

    status = models.CharField(
        'Status',
        max_length=8,
        choices=SALE_STATUSES,
        default='pending',
        blank=False,
        null=False
    )
    buyer = models.ForeignKey(
        User,
        verbose_name='Buyer',
        on_delete=models.CASCADE,
        null=False
    )
    listing = models.ForeignKey(
        Listing,
        verbose_name='Listing',
        on_delete=models.CASCADE,
        null=False
    )
    sale_price = models.IntegerField(
        'Final Sale Price',
        blank=False,
        null=False
    )

    def __str__(self):
        return "Sale of {}".format(self.listing)
