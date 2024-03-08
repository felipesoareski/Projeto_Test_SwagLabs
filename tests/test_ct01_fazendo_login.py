'''Feature: Realizar login no sistema
    Como um usuário
    Eu quero conseguir fazer login no sistema
    Para acessar as funcionalidades disponíveis

    Scenario: Fazendo login com sucesso
        dado que estou na página de login
        quando eu faço login com as credenciais padrão
        entao eu devo ser redirecionado para a página inicial
        '''
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures('setup_teardown')
class Test_CT01:
    def test_ct01_fazendo_login(self):

        login_page = LoginPage()
        home_page = HomePage()
        login_page.fazer_login('standard_user','secret_sauce')

        home_page.verificar_login_com_sucesso()

        # navegador.find_element(By.ID, 'user-name').send_keys('standard_user')
        # navegador.find_element(By.ID, 'password').send_keys('secret_password')
        # navegador.find_element(By.ID, 'button_login').click()
        # assert navegador.find_element(By.XPATH, '//*[@class="product_label"]').is_displayed()
