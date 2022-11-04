from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/gleison/Desktop/pythonProjects/tdd_busca_animal/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_find_new_animal(self):
        """Teste para usuário procurar um animal"""
    # Vini, deseja encontrar um novo animal,
    # para adotar.
       

    # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
    # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca animal', brand_element.text)
    # Ele vê um campo para pesquisar animais pelo nome. 
    
    # Ele pesquisa por Leão e clica no botão pesquisar.

    # O site exibe 4 caracteristicas do animal pesquisado.

    # Ele desiste de adotar um leão.
        pass