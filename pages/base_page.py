import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self) -> None:
        self.navegador = conftest.navegador

    def encontar_elemento(self, locator):
        return self.navegador.find_element(*locator)

    def encontar_elementos(self, locator):
        return self.navegador.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontar_elemento(locator).is_displayed(), f'o elemento "{
            locator}" nao foi encontrado!'

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontar_elemento(locator).text

    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.navegador, timeout).until(EC.presence_of_element_located(locator))

    def verificar_se_elemento_nao_existe(self, locator):
        assert len(self.encontar_elementos(locator)) == 0,  f'Elemento "{
            locator}" existe, mais é esperado que "NÃO" exista.'

    def clique_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.navegador).double_click(element).perform()

    def clique_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.navegador).context_click(element).perform()
