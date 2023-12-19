from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'created',
            'updated',
            'status',
            'seller',
            'starship',
            'sale_price',
            'sold'
        ]
