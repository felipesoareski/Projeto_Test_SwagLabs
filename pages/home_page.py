from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        
        self.navegador = conftest.navegador
        self.titulo_pagina = (By.XPATH, '//*[@class="product_label"]')
        self.item_inventario = (By.XPATH, '//*[@class="inventory_item_name" and text()="{}"]')
        self.adicionar_ao_carrinho = (By.XPATH, '//*[@class="btn_primary btn_inventory"]')
        self.remover_do_carrinho = (By.XPATH, '//*[@class="btn_secondary btn_inventory"]')
        self.icon_carrinho = (By.XPATH, '//*[@class="svg-inline--fa fa-shopping-cart fa-w-18 fa-3x "]')
        self.imagem_produto = (By.CLASS_NAME, 'inventory_details_img')
        
    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def add_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.verificar_se_elemento_existe(self.imagem_produto)
        self.clicar(self.adicionar_ao_carrinho)
        # String de formatação do XPath
    def entrar_no_carrinho(self):
        self.clicar(self.icon_carrinho)
