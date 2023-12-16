from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegar=webdriver.Chrome(service=servico)
navegar.get("https://ri.magazineluiza.com.br/ShowCanal/Planilha-de-Resultado?=CHN0/Z4bUSgrS8IkQeL+Wg==&linguagem=pt%23#")

navegar.find_element(By.XPATH,'//*[@id="LCT0jcMkm6vLyEUX8g5eiA=="]').click()