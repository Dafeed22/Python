import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url_base= "https://www.facebook.com/login.php/"

class Pagina_Inicio:
    def __init__(self,driver):
        self.driver =driver
        self.campo_correo ="email" #name
        self.campo_contraseña = "pass" #name
        self.boton_iniciar_sesion ="login" # name 



        def optener_campo_correo(self):
            return self.driver.find_element(By.NAME, self.campo_correo)
        
        def optener_campo_contraseña(self):
            return self.driver.find_element(By.NAME, self.campo_correo)
        
        def optener_boton_iniciar_sesión(self):
            return self.driver.find_element(By.NAME, self.boton_iniciar_sesion)
        
        def diligenciar_campos(self, campo_correo,campo_contraseña):
            self.optener_campo_correo().send_keys(campo_correo)
            self.optener_campo_contraseña().send_keys(campo_contraseña)
            time.sleep(3)
        
        def clcik_botón_iniciar_sesión(self):
            return self.optener_boton_iniciar_sesión().click()
        
        def optener_url_base(self):
            return url_base
           
