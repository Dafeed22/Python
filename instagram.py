from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver_path = "C:\\Users\\dafee\\DANIEL\\Desktop\\ChromeDriver\\chrome-win64\\chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.instagram.com/")