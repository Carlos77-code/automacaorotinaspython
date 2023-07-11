from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#Criando o Robô
navegador = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#Acessando o site
navegador.get('https://www.pichau.com.br/')

#Maximizando a janela
# navegador.maximize_window()

#Tempo de espera
time.sleep(5)