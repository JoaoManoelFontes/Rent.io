from django.db import IntegrityError
from django.test import TestCase
from ..models import Customer


class ModelTest(TestCase):
    def setUp(self):
        self.customer = {
            "username": "username",
            "password": "password",
            "email": "test@mail.com",
            "instagram": "https://www.instagram.com/test/",
            "phone_number": "+5511999999999",
            "cpf": "12345678901",
        }

    # Model factories
    def create_user(self, **kwargs) -> Customer:
        return Customer.objects.create_user(**self.customer)

    def create_superuser(self, **kwargs) -> Customer:
        return Customer.objects.create_superuser(**self.customer)

    # Tests
    def test_create_user(self):
        """Test creating a new user"""

        user = self.create_user()

        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(user.username, self.customer.get("username"))

    def test_create_superuser(self):
        """Test creating a new superuser"""

        user = self.create_superuser()

        self.assertEqual(user.username, self.customer.get("username"))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_cpf_unique_constraint(self):
        """Test CPF unique constraint"""

        self.create_user()

        with self.assertRaises(IntegrityError):
            self.create_user()
