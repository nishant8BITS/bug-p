from django.test import TestCase
from features.models import Feature
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    def test_get_cart_page(self):
        """
        Test to see if correct page is returned when viewing cart
        """
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
    def test_add_to_cart(self):
        """
        Test to see if an item is added to cart
        """
        admin = User(username="admin")
        admin.save()
        feature = Feature(name="test", description="test", status="done", upvotes=0, views=0,  author=admin)
        feature.save()
        
        page = self.client.get("/cart/add{0}".format(feature.id))
        session = self.client.session
        cart = session['cart']
        
        self.assertEqual(cart, {'1': 1})
        
    def test_adjust_cart(self):
        """
        This tests if when a feature is in a cart than when the adjust view method is run, it deletes the so called feature from the cart
        """
        admin = User(username="admin")
        admin.save()
        feature = Feature(name="test", description="test", status="done", upvotes=0, views=0,  author=admin)
        feature.save()
        session = self.client.session
        page1 = self.client.get("/cart/add{0}".format(feature.id))
        
        page2 = self.client.get("/cart/adjust{0}".format(feature.id))
        session = self.client.session
        cart = session['cart']
        
        self.assertEqual(cart, {})