import pytest
from selenium import webdriver

navegador: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global navegador
    navegador = webdriver.Chrome()
    navegador.get('https://www.saucedemo.com/v1/')
    # navegador.maximize_window()
    navegador.implicitly_wait(5)
    # wait = WebDriverWait(navegador, 10)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="login_logo"]')))

    # run test
    yield

    # teardown
    navegador.quit()
