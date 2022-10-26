"""
proceso-serial.py

Script que lee continuamente el puerto serial y procesa
el texto leido.

El trabajo para ahora (25 octubre) es desde la linea 32
"""


# establecer conexion con puerto serial
# (comentado porque no estamos conectados a un Atmega con un puerto serial)
"""

import serial

ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=0)


while True:
    linea = ser.readline()

"""


"""
Aqui empieza lo que haremos ahora

Objetivo: clasificar las entradas por su valor y empaquetarlas en formato JSON

Ejemplo:
"""
import random
# funcion que simula la entrega de los datos por serial
def serial_read(lista):
    tipo = random.sample(lista, 1)
    linea = tipo[0]
    if tipo == "Ubicacion":
        linea = f"Latitude: {random.normalvariate(120.01, 15)} Longitude: {random.normalvariate(50.01, 15)} Altura {random.normalvariate(750, 40)}"
    else:
        linea = linea + f": {random.normalvariate(20, 3)}"
    return linea

lista = ["temperatura", "co2", "ozono", "presion"]

"""
Walter: 
Definir una funcion que procese los valores de los sensores (en la variable lista) y lo muestre en formato JSON

Ejemplo de entrada salida y procesado:

# entrada:
linea = "temperatura: 25.32"

# salida:
valores = linea.split(":")
json = f"{valores[0]}: {valores[1]}"
json = "{" + json + "}"

Explicacion: linea representa el string que el lora entrega (por puerto serial)
    necesitamos que el string tenga el siguiente formato: 
    JSON = {"temperatura": "23.3"}
    Para esto se parte en 2 la entrada, con el metodo .split(":"), esto genera: ["temperatura","25.32"]
"""

def procesar(linea):
    # codigo aqui
    salida = ""
    return salida

# probar 100 lecturas
for i in range(100):
    linea = serial_read(lista)
    print(procesar(linea))
    