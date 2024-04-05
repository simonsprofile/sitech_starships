from unittest import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Listing, Sale
from starships.models import Starship
from django.contrib.auth.models import User


# Model Tests
class ListingModelCreateTest(TestCase):
    def create_dependent_models(self):
        self.seller = User.objects.create_user(
            'test_username',
            email='test_user@test_user.test',
        )
        self.starship = Starship.objects.create(
            name='Test Starship',
            starship_model='Test Starship Model',
            manufacturer='Test Manufacturer',
            starship_class='Test Starship Class',
            value_when_new=1,
            length=1.0,
            max_atmosphering_speed=1,
            hyperdrive_capacity=1.0,
            min_crew=1,
            max_crew=1,
            passengers=1,
            cargo_capacity=1,
            consumables_for='A test period of time',
            mglt=1
        )

    def create_minimum_listing(self):
        return Listing.objects.create(
            seller_id=self.seller.id,
            starship_id=self.starship.id,
            sale_price=1
        )

    def create_detailed_listing(self):
        return Listing.objects.create(
            status='active',
            seller_id=self.seller.id,
            starship_id=self.starship.id,
            sale_price=1,
            sold=False
        )

    def test_create_min_listing(self):
        self.create_dependent_models()

        minimum_listing = self.create_minimum_listing()
        self.assertTrue(isinstance(minimum_listing, Listing))

        detailed_listing = self.create_detailed_listing()
        self.assertTrue(isinstance(detailed_listing, Listing))


# Endpoint Tests
class ListingRequestTest(APITestCase):
    def url(self):
        return reverse('Listings')

    def create_dependent_models(self):
        self.seller = User.objects.create_user(
            'test_username',
            email='test_user@test_user.test',
        )
        self.starship = Starship.objects.create(
            name='Test Starship',
            starship_model='Test Starship Model',
            manufacturer='Test Manufacturer',
            starship_class='Test Starship Class',
            value_when_new=1,
            length=1.0,
            max_atmosphering_speed=1,
            hyperdrive_capacity=1.0,
            min_crew=1,
            max_crew=1,
            passengers=1,
            cargo_capacity=1,
            consumables_for='A test period of time',
            mglt=1
        )

    def test_get_listings(self):
        response = self.client.get(self.url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_listing(self):
        self.create_dependent_models()
        data = {
            'seller_id': self.seller.id,
            'starship_id': self.starship.id,
            'sale_price': 1
        }
        response = self.client.post(self.url(), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_listing(self):
        self.assertTrue(True)
