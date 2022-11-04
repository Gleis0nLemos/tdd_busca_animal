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
    # Vini, deseja encontrar um novo animal para adotar.
       
    # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')

    # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca animal', brand_element.text)

    # Ele vê um campo para pesquisar animais pelo nome.
        busca_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(busca_input.get_attribute('placeholder'), 'Exemplo: leão, urso...') 
    
    # Ele pesquisa por Leão e clica no botão pesquisar.
        busca_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

    # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

    # Ele desiste de adotar um leão.
        