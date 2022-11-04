from django.test import TestCase, RequestFactory
from animals.models import Animal

class AnimalTest(TestCase):

    def setUp(self):
        
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        )
    
    def test_animal_cadastrado(self):
        """Teste para verificar se o animal buscado está cadastrado com suas respectivas caracteristicas"""

        self.assertEqual(self.animal.nome_animal, 'Leão')