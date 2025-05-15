from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def inicialize_driver():
    driver =webdriver.Edge()
    return driver


def main():
    driver = inicialize_driver()
    driver.get("https://www.mercadolibre.com.co/")
    time.sleep(6)

    if __name__ =='__main__':
        main()