from django.test import TestCase
from .models import Order

# Create your tests here.
class OrderTests(TestCase):
    """
    Here we will define the tests that run against the model Order that are relevant
    """
    def test_date_str(self):
        test_order = Order(full_name= "test", 
                    phone_number= "test", 
                    country="test",
                    postcode= "test",
                    town_or_city= "test",
                    street_address1= "test",
                    street_address2="test",
                    date="2018-12-12")
                    
        self.assertEqual(str(test_order.date), "2018-12-12")