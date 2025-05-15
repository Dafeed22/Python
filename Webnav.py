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
    input_Username = driver.find_element(By.ID,"user-name")
    Container_username = driver.find_element(By.XPATH,'//*[@id="login_credentials"]') 
    split_container_username = Container_username.text.split("\n")
    User_name =split_container_username[1]
    print("Username usuario extraido: \n", User_name)
    input_Username.send_keys(User_name)
    input_password= driver.find_element(By.ID,"password")
    Container_password= driver.find_element(By.CLASS_NAME,'login_password') 
    split_container_password = Container_password.text.split("\n")
    User_password=split_container_password[1]
    print("Password usuario extraido: \n", User_password)
    input_password.send_keys(User_password)
    login_button = driver.find_element(By.ID,"login-button")
    print("botón encontrado_:", login_button)
    login_button.click()
    return driver


def logout(driver):
    menu_button= driver.find_element(By.CLASS_NAME,'bm-burger-button')
    menu_button.click()
    print("Menu button encontrado", menu_button)
    time.sleep(6)
    button_logout = driver.find_element(By.ID,"logout_sidebar_link")
    button_logout.click()
    print("logout sussesfully")
    driver.quit()

    

def main():
    driver= inicialize_driver()
    driver.get("https://www.saucedemo.com/v1/")
    driver =login(driver)
    if driver.current_url == "https://www.saucedemo.com/v1/inventory.html":
        print("Login Successful")
        driver=logout(driver)
    else:
         print("Login Fail")
        
   

if __name__ == '__main__':
    main()