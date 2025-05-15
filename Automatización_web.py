from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options =webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

#Abrir Iniciar Pagina 

def abrir_pagina():
    driver = webdriver.Chrome()
    return driver
def Login(driver):
    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='email']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='pass']")))
    username.clear
    password.clear
    username.send_keys("danielphotos08@gmail.com")
    password.send_keys("961224114401022422525")
    button_login = driver.find_element(By.NAME,"login")
   ## button_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "login")))
    #clic boton iniciar sesión
    button_login.click()
    time.sleep(5)
    return driver


def main():
    driver= abrir_pagina()
    driver.get("https://www.facebook.com/login.php/")
    driver= Login(driver)
   

if __name__ == '__main__':
    main()   