from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animals.models import Animal

class indexViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Calopsita',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim',
        )

    def test_return_caract_animals(self):
        """Teste de verificação se a index retorna as características do animal pesquisado"""

        response = self.client.get('/',
            {'buscar': 'Calopsita'},
        )
        caracteristicas_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristicas_animal_pesquisado[0].nome_animal, 'Calopsita')