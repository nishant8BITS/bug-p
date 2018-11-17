from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestUserLoginForm(TestCase):
    
    def test_can_login_with_required_values(self):
        form = UserLoginForm({'username_or_email': 'Test', 'password': 'create a test'})
        self.assertTrue(form.is_valid())
        
    def test_cannot_login_with_required_values(self):
        form = UserLoginForm({'username_or_email': 'Test'})
        self.assertFalse(form.is_valid())
        
        
class TestUserRegistrationForm(TestCase):
    
    def test_can_create_a_user_with_required_values(self):
        form = UserRegistrationForm({'username':'test','email':'test@admin.com','password1':'testpassword','password2':'testpassword'})
        self.assertTrue(form.is_valid())
        
    def test_cannot_create_a_user(self):
        """
        error is passwords don't match
        """
        form = UserRegistrationForm({'username':'test','email':'test@admin.com','password1':'testpassword','password2':'testpasswor'})
        self.assertFalse(form.is_valid())