from django.contrib.contenttypes.models import ContentType
from ..models import House, Building, Apartment, Media, Payment  # noqa
from django.test import TestCase
from core.models import Customer


class ModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username="username", password="password"
        )

        self.house = {
            "customer": self.customer,
            "address": "Rua dos Bobos, 0",
            "city": "São Paulo",
            "description": "Casa com quintal",
            "garage": True,
            "backyard": True,
            "pool": True,
            "rooms": 3,
            "bathrooms": 2,
            "suites": 1,
            "area": 100,
            "price": 1000.00,
        }

        self.building = {
            "customer": self.customer,
            "address": "Rua dos Bobos, 0",
            "city": "São Paulo",
            "description": "Prédio com elevador",
            "name": "Prédio do " + self.customer.username,
            "recreation_area": True,
            "elevator": True,
            "concierge": True,
            "floors": 7,
        }

        self.apartment = {
            "floor": 1,
            "number": 1,
            "rooms": 3,
            "bathrooms": 2,
            "suites": 1,
            "area": 100,
            "price": 1000.00,
        }

        self.payment = {
            "date": "2020-01-01",
            "next_payment": "2020-02-01",
        }

    # Model Factories
    def create_house(self, **kwargs):
        """Create a house with the given kwargs"""
        return House.objects.create(**self.house, **kwargs)

    def create_building(self, **kwargs):
        """Create a building with the given kwargs"""
        return Building.objects.create(**self.building, **kwargs)

    def create_apartment(self, **kwargs):
        """Create an apartment with the given kwargs"""

        return Apartment.objects.create(**self.apartment, **kwargs)

    def create_payment(self, **kwargs):
        """Create a payment with the given kwargs"""
        return Payment.objects.create(**self.payment, **kwargs)

    # Tests
    def test_create_house(self):
        """Test creating a new house"""
        self.create_house()

        self.assertEqual(House.objects.count(), 1)
        self.assertEqual(House.objects.filter(customer=self.customer).count(), 1)

    def test_create_building(self):
        """Test creating a new building"""
        self.create_building()

        self.assertEqual(Building.objects.count(), 1)
        self.assertEqual(Building.objects.filter(customer=self.customer).count(), 1)

    def test_create_apartment(self):
        """Test creating a new apartment"""
        building = self.create_building()
        self.create_apartment(building=building)

        self.assertEqual(Apartment.objects.count(), 1)
        self.assertEqual(Apartment.objects.filter(building=building).count(), 1)

    def test_create_payment(self):
        """Test creating a new payment to a house and an apartment"""
        house = self.create_house()
        self.create_payment(value=house.price, content_object=house)

        apartment = self.create_apartment(building=self.create_building())
        self.create_payment(value=apartment.price, content_object=apartment)

        self.assertEqual(Payment.objects.count(), 2)

        self.assertEqual(
            Payment.objects.filter(
                content_type=ContentType.objects.get_for_model(apartment),
                object_id=apartment.id,
            ).count(),
            1,
        )

    def test_add_media_to_house(self):
        """Test adding a media to a house"""
        house = self.create_house()
        Media.objects.create(
            image="./static/images/house.jpg",
            content_object=house,
        )

        apartment = self.create_apartment(building=self.create_building())
        Media.objects.create(
            video="https://www.youtube.com/watch?v=9bZkp7q19f0",
            content_object=apartment,
        )

        self.assertEqual(Media.objects.count(), 2)
        self.assertEqual(
            Media.objects.filter(
                content_type=ContentType.objects.get_for_model(house),
                object_id=house.id,
            )[0],
            Media.objects.first(),
        )
