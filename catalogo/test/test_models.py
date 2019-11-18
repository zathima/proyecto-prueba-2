from django.test import TestCase
from catalogo.models import Persona

class UserModelTest(TestCase):

    def setUp(self):
        self.test_persona = Persona(field_email="prueba@prueba.com", field_name='test persona')
        self.test_persona.save()

    def test_user_to_string_email(self):
        self.assertEquals(str(self.test_persona), "prueba@prueba.com")

    def test_get_by_id(self):
        self.assertEquals(Persona.get_by_id(1), self.test_persona)

    def tearDown(self):
        self.test_persona.delete()