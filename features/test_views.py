from django.test import TestCase
from .models import Feature, FeatureComment
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    def test_get_features_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
    def test_add_feature_page(self):
        page = self.client.get("/features/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_feature.html")
        
    def test_view_feature_page(self):
        admin = User(username="admin")
        admin.save()
        feature = Feature(name="test", description="test", status="done", upvotes=0, views=0,  author=admin)
        feature.save()
        
        page = self.client.get("/features/{0}/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature_detail.html")