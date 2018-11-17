from django.test import TestCase
from .models import Bug

# Create your tests here.
class BugTests(TestCase):
    """
    Here we will define the tests that run against the model Bug
    """
    def test_name_str(self):
        test_name = Bug(name="A test bug")
        self.assertEqual(str(test_name), "A test bug")