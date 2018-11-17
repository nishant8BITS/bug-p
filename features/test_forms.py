from django.test import TestCase
from .forms import FeatureForm, FeatureCommentForm

class TestFeatureForm(TestCase):
    
    def test_can_create_a_feature_with_required_values(self):
        form = FeatureForm({'name': 'Test', 'description': "create a test"})
        self.assertTrue(form.is_valid())
        
    def test_cannot_create_a_feature_with_required_values(self):
        form = FeatureForm({'name': 'Test'})
        self.assertFalse(form.is_valid())
        
        
class TestFeatureCommentForm(TestCase):
    
    def test_can_create_a_comment_with_required_values(self):
        form = FeatureCommentForm({'description': "i am a test comment"})
        self.assertTrue(form.is_valid())
        
    def test_if_comment_can_be_integer(self):
        form = FeatureCommentForm({'description': 1})
        self.assertTrue(form.is_valid())