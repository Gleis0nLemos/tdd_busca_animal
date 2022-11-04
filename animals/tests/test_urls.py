from django.test import TestCase, RequestFactory
from django.urls import reverse
from animals.views import index

class animalsURLsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_root_view_index(self):
        
        """Teste se a home utiliza a view index"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):      
            response = index(request)
            self.assertEqual(response.status_code, 200)
 