from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

#Abrir un sitio

driver.get("http://www.google.com/")

#Esperar un momento mientras carga la página

time.sleep(3)

#Buscar
busqueda= driver.find_element(By.NAME, "q")
busqueda.send_keys("descuentos")
busqueda.send_keys(Keys.RETURN)
time.sleep(3)


#scroll down
 
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()