from django.test import TestCase
from .models import User, Project, Article

# Create your tests here.

class TestUser(TestCase):
    
    def setUp(self) -> None:
        user = User.objects.create(login='semenovse', last_name='Семенов', first_name='Семен', patronymic='Евгеньевич')


    def test_init(self):
        self.assertEqual(self.login, 'semenovse')
