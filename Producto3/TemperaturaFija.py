import time
import requests
import sys

#Ficha para la conexion
token = ""  #---------INTRODUCIR UN TOKEN POR DEFECTO
if len(sys.argv) == 2:
    token = sys.argv[1] #---------INTRODUCIR UN TOKEN AL EJECUTAR EL SCRIPT DESDE CONSOLA
#Primera parte de la URL
URL_PART1 = "https://demo.thingsboard.io/api/v1/"
#Segunda parte de la URL
URL_PART2 = "/telemetry"
#Union de las partes de la URL con la ficha
URL = URL_PART1 + token + URL_PART2
#Definir tipo de fichero que se envia en el POST
HEADERS = {"Content-Type": "application/json"}
#Bucle infinito que genera el mensaje, lo envia e imprime el estado de la conexion
while True:
    #Genera el JSON a enviar
    datos = {'temperature': 23}
    #Envio del JSON a la URL indicando el tipo de fichero
    r = requests.post(URL, headers=HEADERS, json=datos)
    #Imprime el resultado del envio del mensaje
    print("Codigo de estado de la conexion", r.status_code)
    #Para la ejecucion 2 segundos
    time.sleep(2)
    
