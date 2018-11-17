from django.test import TestCase
from .forms import BugForm, BugCommentForm

class TestBugForm(TestCase):
    
    def test_can_create_a_bug_with_required_values(self):
        form = BugForm({'name': 'Test', 'description': "create a test"})
        self.assertTrue(form.is_valid())
        
    def test_cannot_create_a_bug_with_required_values(self):
        form = BugForm({'name': 'Test'})
        self.assertFalse(form.is_valid())
        
        
class TestBugCommentForm(TestCase):
    
    def test_can_create_a_comment_with_required_values(self):
        form = BugCommentForm({'description': "i am a test comment"})
        self.assertTrue(form.is_valid())
        
    def test_if_comment_can_be_integer(self):
        form = BugCommentForm({'description': 1})
        self.assertTrue(form.is_valid())