import time 
from src.Page_Object_Model.Pages import page_login_home
from src.Test_Base.Webdriver_Setup import Webdriver_Setup
  
class pruerba_login(Webdriver_Setup):
     
     def iniciarsesión(self):
          self.driver.get(page_login_home.geturl_base())
          pagina_inicio =page_login_home(driver)
          time.sleep(3)
          pagina_inicio.diligenciar_campos("danielphotos08@gmail.com", "password?")
          pagina_inicio.click_boton_iniciar_sesion()
          


          
  
