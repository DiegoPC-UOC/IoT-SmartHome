
import paho.mqtt.client as paho
import random
import time
import sys

#Variables de conexion con la información por defecto
broker="localhost"
port=1883
#Comprueba si el usuario ha intoducido dos parametros desde la consola al ejecutar el script
if len(sys.argv) == 3:
    #Si lo hace asigna el primer parametro como la ip del host de destino
    broker = sys.argv[1]
    #Y el segundo parametro como el puerto de destino
    port =  int(sys.argv[2])
#Funcion que genera un numero aleatorio en un rango dado para los lux
def generarLux():
    lux = random.randrange(50,10000)
    mensaje = lux
    return lux
#Funcion que recoge un cliente y envia un mensaje a su nombre, con el valor de lux generado anteriormente
def envioMensajeLux(cliente,topico):
    lumen = generarLux()
    #Concatenacion del mensaje
    mensaje = str(lumen)
    #Envío del mensaje
    cliente.publish(topico, mensaje)
    cliente.loop
#Creacion de clientes para el envio de temperaturas asignandoles un nombre
clienteLuz1 = paho.Client("HabitacionLumen1")
topico = "casa/luz/habitacion"
#Creacion de la conexion para los clientes
clienteLuz1.connect(broker, port)
#Bucle infinito para el envio de mensajes
while True:
    envioMensajeLux(clienteLuz1,topico)
    #Parar la ejecucion del script 5 segundos
    time.sleep(2)
