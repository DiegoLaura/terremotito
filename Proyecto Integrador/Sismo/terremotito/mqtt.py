###################################
###     MQTT INSERTA A MYSQL    ###
###################################

import sys 
import paho.mqtt.client as mqtt
import pymysql

# Configuración MQTT
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "terremotito"

# Función para manejar los mensajes MQTT
def on_message(client, userdata, msg):
    #Recibe el mensaje 
    payload = msg.payload.decode("utf-8")
    print("Mensaje recibido: " + payload)
    
    try:
        dato = int(payload)
        insertar_movimiento(dato)
    
    except ValueError:
        print("no funciona")

def insertar_movimiento(dato):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='terremotito'
    )
    query = f"SELECT * FROM terremotito_intensidad WHERE movimiento={dato}"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        
    if result: 
        print("el dato ya esta dentro")
    else:
        query = f"INSERT INTO terremotito_intensidad (tiempo, movimiento) VALUES (NOW(), {dato})"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
        print("Registrado")
    connection.close()

# Configuración del cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)
mqtt_client.subscribe(mqtt_topic)
mqtt_client.on_message = on_message

# Iniciar el bucle de recepción de mensajes MQTT
mqtt_client.loop_forever()