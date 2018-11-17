from django.test import TestCase
import json

# Create your tests here.
class TestViews(TestCase):
    def test_get_graph_page(self):
        """
        Test to see if graph/community page is returned
        """
        page = self.client.get("/graphs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "graphs.html")
        
    def test_to_see_ajax_request(self):
        """
        Test to see if ajax view returns correct data (To test query values in ajax response you need to populate test database.)
        """
        response = self.client.post('/graphs/api/data/', content_type='application/json')
        json_string = response.content
        json_string = response.content
        response_data = json.loads(str(response.content, encoding='utf8'))
        self.assertEquals(response_data["labels1"], ["Users", "Bugs", "Features"])