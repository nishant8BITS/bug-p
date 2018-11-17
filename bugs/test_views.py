from django.test import TestCase
from .models import Bug, BugComment
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    def test_get_bugs_page(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
        
    def test_add_bug_page(self):
        page = self.client.get("/bugs/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_bug.html")
        
    def test_view_bug_page(self):
        admin = User(username="admin")
        admin.save()
        bug = Bug(name="test", description="test", status="done", upvotes=0, views=0,  author=admin)
        bug.save()
        
        page = self.client.get("/bugs/{0}/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug_detail.html")
        
    def test_upvote_bug(self):
        admin = User(username="admin")
        admin.save()
        bug = Bug(name="test", description="test", author=admin)
        bug.save()
        
        page = self.client.post("/bugs/upvote{0}/".format(bug.id))
        bug.refresh_from_db()
        self.assertEqual(page.status_code, 302)
        self.assertEqual(bug.upvotes, 1)
        