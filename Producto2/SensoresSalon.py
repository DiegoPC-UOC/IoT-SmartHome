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
#Funcion que genera un numeo aleatorio en un rango dado para la temperatura y humedad. Devuelve los dos valores
def generarTemperatura():
    temp = random.randrange(0,34)
    return temp
#Funcion que genera un numeo aleatorio en un rango dado para la temperatura y humedad. Devuelve los dos valores
def generarHumedad():
    humd = random.randrange(25,55)
    return humd
#Funcion que genera un numero aleatorio en un rango dado para los lux
def generarLux():
    lux = random.randrange(50,10000)
    mensaje = lux
    return lux
#Funcion que recoge un cliente y envia un mensaje a su nombre, con los valores de temperatura y humedad generados anteriormente
def envioMensajeTemperatura(cliente,topico):
    #Almacena los valores aleatorios
    temp = generarTemperatura()
    #Concatenacion del mensaje
    mensaje = str(temp)
    #Envío del mensaje
    cliente.publish(topico, mensaje)
    #Mantiene abierta la conexion
    cliente.loop
def envioMensajeHumedad(cliente,topico):
    #Almacena los valores aleatorios
    humd = generarHumedad()
    #Concatenacion del mensaje
    mensaje = str(humd)
    #Envío del mensaje
    cliente.publish(topico, mensaje)
    #Mantiene abierta la conexion
    cliente.loop
#Funcion que recoge un cliente y envia un mensaje a su nombre, con el valor de lux generado anteriormente
def envioMensajeLux(cliente,topico):
    lumen = generarLux()
    #Concatenacion del mensaje
    mensaje = str(lumen)
    #Envío del mensaje
    cliente.publish(topico, mensaje)
    cliente.loop
#Creacion de clientes para el envio de temperaturas asignandoles un nombre
clienteTemp1 = paho.Client("SalonTemp1")
clienteTemp2 = paho.Client("SalonTemp2")
clienteTemp3 = paho.Client("SalonTemp3")
clienteTemp4 = paho.Client("SalonTemp4")
clienteHumd1 = paho.Client("SalonHum1")
clienteHumd2 = paho.Client("SalonHum2")
clienteHumd3 = paho.Client("SalonHum3")
clienteHumd4 = paho.Client("SalonHum4")
clienteLuz1 = paho.Client("SalonLumen1")
clienteLuz2 = paho.Client("SalonLumen2")
clienteLuz3 = paho.Client("SalonLumen3")
clienteLuz4 = paho.Client("SalonLumen4")

topico1 = "casa/temperatura/salon/s1"
topico2 = "casa/temperatura/salon/s2"
topico3 = "casa/temperatura/salon/s3"
topico4 = "casa/temperatura/salon/s4"

topico5 = "casa/humedad/salon/s1"
topico6 = "casa/humedad/salon/s2"
topico7 = "casa/humedad/salon/s3"
topico8 = "casa/humedad/salon/s4"

topico9 = "casa/luz/salon/s1"
topico10 = "casa/luz/salon/s2"
topico11 = "casa/luz/salon/s3"
topico12 = "casa/luz/salon/s4"

#Creacion de la conexion para los clientes
clienteTemp1.connect(broker, port)
clienteTemp2.connect(broker, port)
clienteTemp3.connect(broker, port)
clienteTemp4.connect(broker, port)

clienteHumd1.connect(broker, port)
clienteHumd2.connect(broker, port)
clienteHumd3.connect(broker, port)
clienteHumd4.connect(broker, port)

clienteLuz1.connect(broker, port)
clienteLuz2.connect(broker, port)
clienteLuz3.connect(broker, port)
clienteLuz4.connect(broker, port)
#Bucle infinito para el envio de mensajes
while True:
    envioMensajeTemperatura(clienteTemp1,topico1)
    envioMensajeTemperatura(clienteTemp2,topico2)
    envioMensajeTemperatura(clienteTemp3,topico3)
    envioMensajeTemperatura(clienteTemp4,topico4)
    #Parar la ejecucion del script 2 segundos
    time.sleep(2)

    envioMensajeHumedad(clienteHumd1,topico5)
    envioMensajeHumedad(clienteHumd2,topico6)
    envioMensajeHumedad(clienteHumd3,topico7)
    envioMensajeHumedad(clienteHumd4,topico8)
    #Parar la ejecucion del script 2 segundos
    time.sleep(2)

    envioMensajeLux(clienteLuz1,topico9)
    envioMensajeLux(clienteLuz1,topico10)
    envioMensajeLux(clienteLuz1,topico11)
    envioMensajeLux(clienteLuz1,topico12)
    #Parar la ejecucion del script 2 segundos
    time.sleep(2)
