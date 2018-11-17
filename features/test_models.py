from django.test import TestCase
from .models import Feature

# Create your tests here.
class BugTests(TestCase):
    """
    Here we will define the tests that run against the model Bug
    """
    def test_name_str(self):
        test_name = Feature(name="A test feature")
        self.assertEqual(str(test_name), "A test feature")