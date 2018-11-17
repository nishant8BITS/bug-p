from django.test import TestCase

class TestViews(TestCase):
    def test_get_home_page(self):
        """
        Test to see if correct page is returned when viewing home
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")