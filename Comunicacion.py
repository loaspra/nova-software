import json
import random
from tkinter.ttk import Separator
from turtle import end_fill
import serial

i=0

class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('ANSI')
        return json.JSONEncoder.default(self, obj)


estructura={}
def gjson(linea):
    #valores=linea.split(":")
    with open('bd_cansat.json','w') as archivo:
        json.dump(linea,archivo,separators=(",",":"),cls=BytesEncoder)
        x=print("Archivo generado")

    return x

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    #parity=serial.PARITY_NONE,
    #stopbits=serial.STOPBITS_ONE,
    #bytesize=serial.EIGHTBITS,
    #timeout=0
    )
while i!=80:
    linea = ser.readline()
    estructura[i]=linea
    i=i+1
    
gjson(estructura)


