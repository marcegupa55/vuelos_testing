from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

#Abrir un sitio


driver.get("file:///C:/Users/julie/OneDrive/Documentos/MARCELA/ESPECIALIZACION/SEGUNDO SEMESTRE/INGENIERIA DE SOFTWARE II/NUEVOPROYECTO/ProyIng.html")

#Esperar un momento mientras carga la página

time.sleep(5)



#Ingresar elementos
input_element = driver.find_element_by_id("nombres")

input_element = driver.f

input_element = dr
# Ingresa información en el campo de entrada
input_element.send_keys(
input_element.send_k
'Texto a ingresar')

time.sleep(3)

driver.quit()