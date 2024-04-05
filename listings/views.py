from datetime import datetime

from django.db.models import Q
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Listing
from .serializers import ListingSerializer


class ListingsList(APIView):
    def get(self, request, format=None):
        try:
            highest_price = Listing.objects.order_by(
                '-sale_price'
            ).first().sale_price
        except AttributeError:
            highest_price = 0

        sold = request.GET.get('sold', False)
        status = request.GET.get('status', 'active')
        added_since = request.GET.get('added_since', datetime.min)
        added_before = request.GET.get('added_before', datetime.now())
        price_above = request.GET.get('price_above', 0)
        price_below = request.GET.get('price_below', highest_price)
        seller_id = request.GET.get('seller_id', False)
        starship_id = request.GET.get('starship_id', False)
        starship_class = request.GET.get('starship_class', False)
        sort = request.GET.get('sort_by', '-created')

        seller_ids_str = request.GET.get('seller_ids[]', '')
        seller_ids = [int(x) for x in seller_ids_str.split(',') if x != '']

        starship_ids_str = request.GET.get('starship_ids[]', '')
        starship_ids = [int(x) for x in starship_ids_str.split(',') if x != '']

        filters = Q(
            sold=sold,
            status=status,
            created__gte=added_since,
            created__lt=added_before,
            sale_price__gte=price_above,
            sale_price__lte=price_below,
        )

        if seller_id:
            filters &= Q(seller=seller_id)
        elif len(seller_ids):
            filters &= Q(seller__in=seller_ids)
        if starship_id:
            filters &= Q(starship=starship_id)
        elif len(starship_ids):
            filters &= Q(starship__in=starship_ids)
        elif starship_class:
            filters &= Q(starship__starship_class=starship_class)

        listings = Listing.objects.filter(filters).order_by(sort)

        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingsDetail(APIView):
    def get_object(self, id):
        try:
            return Listing.objects.get(id=id)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        listing = self.get_object(id)
        serializer = ListingSerializer(listing)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        listing = self.get_object(id)
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        listing = self.get_object(id)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
