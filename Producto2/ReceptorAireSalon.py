import paho.mqtt.client as mqtt
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
#Sobrescribe el método on_message para agregar otro comportamiento
def on_message(client, userdata, message):
    #Imprime el mensaje recibido
    print("mensaje recivido: "+str(message.payload.decode("utf-8")))
    #Imprime el topico desde el que se envia el mensaje
    print("topico del mensaje: "+message.topic)

#Crea el cliente asignandole un nombre
client = mqtt.Client("EmisorIR")
#Asigna el metodo que acabamos de sobreescribir
client.on_message = on_message
#Asigna parametros de conexion
client.connect(broker, port)
#Se suscribe al topico necesario
client.subscribe("casa/receptor/aire")
#Queda a la escucha de mensajes de forma infinita
client.loop_forever()
