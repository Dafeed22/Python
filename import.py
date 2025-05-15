from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options= Options()
options =webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

#abrir iniciar pagina

def iniciar_web():
    driver= webdriver.Chrome()
    return driver


def main():
    driver= iniciar_web()
    driver.get("https://www.facebook.com/login.php/")

if __name__ == '__main__':
    main()


