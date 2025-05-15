from ast import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

options =webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

def inicialize_driver():
    driver = webdriver.Chrome()
    return driver
def login(driver):
    username = driver.find_element(By.ID,"user-name")
    user ="performance_glitch_user"
    username.send_keys(user)
    print("Usuario ingresado es :" ,user)
    password ="secret_sauce"
    imput_password = driver.find_element(By.ID,"password")
    imput_password.send_keys(password)
    print("la contraseña ingresada es :", password)
    Button_Click_Login = driver.find_element(By.CLASS_NAME, "btn_action")
    print("este es el boton", Button_Click_Login)
    Button_Click_Login.click()
    return driver


def comprar(driver):
    producto = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    nombre_procucto =producto.text
    print("este es el nombre del producto seleccionado:" ,nombre_procucto)
    button_add_cart = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button")
    nombre_botón =button_add_cart.text
    print("este es el botón", nombre_botón)
    button_add_cart.click()
    



def main():
    driver= inicialize_driver()
    driver.get("https://www.saucedemo.com/v1/")
    driver = login(driver)   
    if driver.current_url == "https://www.saucedemo.com/v1/inventory.html":
        print("Login Successful")
    else:
         print("Login Fail")
    driver = comprar(driver)
    time.sleep(5)
    print(f'ejecución finalizada')


if __name__ == '__main__':
    main()    