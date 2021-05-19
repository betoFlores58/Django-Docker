from django.test import SimpleTestCase

class UsaurioTestCase(SimpleTestCase):
    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Homepage')

    def test_homepage_template(self): 
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'home.html')  
