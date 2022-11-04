from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/gleison/Desktop/pythonProjects/tdd_busca_animal/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_open_window(self):
        self.browser.get(self.live_server_url)

    def test_fail(self):
        '''teste de falha'''
        self.fail('Fail')