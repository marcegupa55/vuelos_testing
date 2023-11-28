from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#Abrir un sitio

driver.get("http://localhost:4200/")

#Esperar un momento mientras carga la página

time.sleep(5)

#Buscar
busqueda= driver.find_element(By.NAME, "q")
busqueda.send_keys("hdtb-mitem hdtb-msel")
busqueda.send_keys(Keys.RETURN)
time.sleep(5)


#Seleccionar menu
 
# Identificar el botón por su selector (puedes utilizar diferentes estrategias según el HTML del botón)
selector_del_boton = "imágenes"  # Cambia esto con el selector real del botón

# Esperar un poco para asegurarse de que la página haya cargado completamente (opcional)
driver.implicitly_wait(2)  # Espera 10 segundos (puedes ajustar el tiempo según sea necesario)

# Seleccionar el botón por su selector
boton = driver.find_element(By.CSS_SELECTOR, selector_del_boton)

# Hacer clic en el botón
boton.click()