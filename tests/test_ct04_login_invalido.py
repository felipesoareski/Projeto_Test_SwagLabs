# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import conftest
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login_invalido
class Test_CT04:
    def test_ct04_login_invalido(self):
        mensagem_erro_esperada = 'Epic sadface: Username and password do not match any user in this service'
        login_page = LoginPage()

        login_page.fazer_login('standard_user', 'senha_incorreta')
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)


        # assert navegador.find_element(By.XPATH, '//*[@data-test="error"]').is_displayed()
