from selenium.webdriver.common.by import By
import conftest
import pytest


@pytest.mark.usefixtures('setup_teardown')
class Test_CT03:
    def test_ct03_compra_produtos(self):
        navegador = conftest.navegador

        # user_name
        navegador.find_element(By.ID, 'user-name').send_keys('standard_user')

        # senha
        navegador.find_element(By.ID, 'password').send_keys('secret_sauce')

        # login_button
        navegador.find_element(By.ID, 'login-button').click()

        # adding to carrinho
        navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').click()

        # clicar no botao add_carrinho e confere se o botao muda para remove
        add_to_cart = navegador.find_element(By.XPATH, '//*[@class="btn_primary btn_inventory"]')
        assert add_to_cart.is_displayed()
        add_to_cart.click()

        remove_button =  navegador.find_element(By.XPATH, '//*[@class="btn_secondary btn_inventory"]')
        assert remove_button.is_displayed()

        # entra no carrinho e confere se o item foi adicionado
        carrinho = navegador.find_element(By.XPATH, '//*[@class="svg-inline--fa fa-shopping-cart fa-w-18 fa-3x "]')
        carrinho.click()
        assert navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()

        # add mais um produto ao carrinho
        navegador.find_element(By.XPATH, '//a[@class="btn_secondary"]').click()
        navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Fleece Jacket"]').click()

        # verificando se a imaigem e o botao add_to_cart foram mostrados
        assert navegador.find_element(By.XPATH, '//*[@class="inventory_details_img"]').is_displayed()
        assert navegador.find_element(By.XPATH, '//*[@class="btn_primary btn_inventory"]').is_displayed()

        # clica no botao add_to_cart e verifica se o botao mudou para remove
        navegador.find_element(By.XPATH, '//*[@class="btn_primary btn_inventory"]').click()
        assert navegador.find_element(By.XPATH, '//*[@class="btn_secondary btn_inventory"]').is_displayed()
        print('passed')

        carrinho = navegador.find_element(By.XPATH, '//*[@class="svg-inline--fa fa-shopping-cart fa-w-18 fa-3x "]')
        carrinho.click()
        assert navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()
        assert navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Fleece Jacket"]').is_displayed()
        print('passed')

        # realizando a compra dos produtos

        navegador.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[2]').click()
        target_text = navegador.find_element(By.XPATH, '//*[@class="subheader"]').text
        assert target_text == 'Checkout: Your Information'
        print('checkout your info > passed')

        # preencendo dados
        navegador.find_element(By.ID, 'first-name').send_keys('primeiro nome')
        navegador.find_element(By.ID, 'last-name').send_keys('ultimo nome')
        navegador.find_element(By.ID, 'postal-code').send_keys('123456789')
        navegador.find_element(By.XPATH, '//*[@class="btn_primary cart_button"]').click()
        target_text = navegador.find_element(By.XPATH, '//*[@class="subheader"]').text
        assert target_text == 'Checkout: Overview'

        # finalizando
        navegador.find_element(By.XPATH,'//*[@class="btn_action cart_button"]').click()
        target_text = navegador.find_element(By.XPATH, '//*[@class="complete-text"]').text
        assert 'Your order has been dispatched' in target_text
        print('finish')
