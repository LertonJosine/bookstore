from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.

class PagesTest(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse('home')
        self.resp = self.client.get(url)
    
    def test_home_page_url(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_home_page_view_uses_correct_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')
    
    def test_home_page_url_name(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_home_page_url_resolves_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
        