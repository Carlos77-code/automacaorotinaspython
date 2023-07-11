from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.dependencias import navegador
import time

class ValorDoProduto:
    def __init__(self, navegador):
        self.navegador = navegador

    def busca_produto(self, logo, nomeBotao, maisUmClick, outroClick):
        wait = WebDriverWait(navegador, 2)
        element = wait.until(EC.presence_of_element_located((By.XPATH, logo)))
        self.click_botao(nomeBotao)
        time.sleep(1)
        self.click_botao(maisUmClick)
        time.sleep(1)
        self.click_botao(outroClick)
        return element  
        

        
        

    def click_botao(self, nomeBotao):
        click_button = self.navegador.find_element(By.XPATH, nomeBotao)
        click_button.click()