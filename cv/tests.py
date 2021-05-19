from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User

class SuperUserTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='pruebaSuper',password='12345abc!',email='')

    def testUser(self):
        usr=User.objects.all()

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='pruebaNormal',password='12345abc!!',email='prueba@gmail.com')

    def testUser(self):
        usr=User.objects.all()

class UsaurioTestCase(SimpleTestCase):
    #ESTE DEBE FALLAR.!!!!!!
    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Homepage')

    def test_homepage_template(self): 
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'home.html')  
