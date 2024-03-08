import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.carrinho
class Test_CT02:
   
    def test_ct02_add_to_carrinho(self):

        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = 'Sauce Labs Backpack'
        produto_2 = 'Sauce Labs Fleece Jacket'

        # fazendo login
        login_page.fazer_login('standard_user', 'secret_sauce')
        
        # adding to carrinho
        home_page.add_ao_carrinho(produto_1)
        # verifica se o botao add to cart muda para remove
        carrinho_page.verifica_botao_remove_aparece()
        #verificar se elemento esta no carrinho
        home_page.entrar_no_carrinho()
        carrinho_page.verificar_produto_existe_no_carrinho(produto_1)
        carrinho_page.clicar_continuar_comprando()
        #adicionar mais um item ao carrinho
        home_page.add_ao_carrinho(produto_2)
        home_page.entrar_no_carrinho()
        carrinho_page.verificar_produto_existe_no_carrinho(produto_2)
        carrinho_page.verificar_produto_existe_no_carrinho(produto_1)
        