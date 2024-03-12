from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class ProductPage(BasePage):
    
    def __init__(self):
        super().__init__()

        self.navegador = conftest.navegador
        self.imagem_produto = (By.CLASS_NAME, 'inventory_details_img')
        self.botao_back = (By.CLASS_NAME, 'inventory_details_back_button')


    def verificar_imagem_existe(self):
        self.esperar_elemento_aparecer(self.imagem_produto)
        self.verificar_se_elemento_existe(self.imagem_produto)

    def verificar_botao_back_existe(self):
        self.verificar_se_elemento_existe(self.botao_back)