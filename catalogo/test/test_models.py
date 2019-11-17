from catalogo.models import Persona

class testmodels(simpletestcase):

	@classmethod		
	def setUpTestData(cls):
        Persona.objects.create(field_name='Matias', field_last_name='Cerpa')

    def test_field_name_label(self):
        persona=Persona.objects.get(id=1)
        field_label = persona._meta.get_field('field_name').verbose_name
        self.assertEquals(field_label,'nombre de la persona')

    def test_char_of_password_label(self):
        persona=Persona.objects.get(id=1)
        field_label = persona._meta.get_field('char_of_password').verbose_name
        self.assertEquals(field_label,'contraseña')

    def test_field_name_max_length(self):
        persona=Persona.objects.get(id=1)
        max_length = persona._meta.get_field('field_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_field_last_name_comma_field_name(self):
        persona=Persona.objects.get(id=1)
        expected_object_name = '%s, %s' % (persona.field_last_name, persona.field_name)
        self.assertEquals(expected_object_name,str(persona))

    def test_get_absolute_url(self):
    	persona=Persona.objects.get(id=1)
    	self.assertEquals(persona.get_absolute_url(),'/catalogo/persona/1')