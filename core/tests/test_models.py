from django.test import TestCase
from ..models import Customer


class ModelTest(TestCase):
    def setUp(self):
        self.customer = {
            "username": "username",
            "password": "password",
            "email": "test@mail.com",
            "phone_number": "+5511999999999",
            "birth_date": "1990-01-01",
            "full_name": "Full Name",
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
