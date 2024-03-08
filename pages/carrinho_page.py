from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CarrinhoPage(BasePage):
    
    def __init__(self):
        super().__init__()
        
        self.navegador = conftest.navegador
        self.item_inventario = (By.XPATH, '//*[@class="inventory_item_name" and text()="{}"]')
        self.botao_continuar_comprando = (By.XPATH, '//a[@class="btn_secondary" and text()="Continue Shopping"]')
        self.botao_remove = (By.XPATH, '//*[@class="btn_secondary btn_inventory" and text()="REMOVE"]')

    def verificar_produto_existe_no_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)
    
    def verifica_botao_remove_aparece(self):
        self.verificar_se_elemento_existe(self.botao_remove)