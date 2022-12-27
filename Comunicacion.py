import json
import random
from tkinter.ttk import Separator
from turtle import end_fill
import serial
import re
i=1
r=0
lon=0
temperatura=[]
humedad=[]
ppmmq=[]
ppmmics=[]

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
while i!=10:
    linea = ser.readline()
    linea = linea.decode("ANSI")
    i=i+1
    r=0
    a=0
    lon=0
    #linea=linea[1:]
    valores=linea.split('|')
    for j in range(len(valores)):
        valores[j]=re.sub("[^0-9,.,-]", "", valores[j])
    temperatura.append(float(valores[0]))
    humedad.append(float(valores[0]))
    ppmmq.append(float(valores[0]))
    ppmmics.append(float(valores[0]))


dinfo={"temperatura": temperatura,
        "humedad": humedad,
        "ppm-mq": ppmmq,
        "ppm-mics": ppmmics,
}
print(temperatura)
print(linea)
gjson(dinfo)


"""for j in linea:
        a=a+1
        if(j=='|'):
            r=r+1
            if r==1:
                temperatura.append(float(linea[0:a-1]))
                lon=len(linea[0:a])
            elif r==2:
                humedad.append(float(linea[lon:a-1]))
                lon=len(linea[lon:a])
            elif r==3:
                ppmmq.append(linea[lon:a])
                lon=len(linea[lon:a])
            elif r==4:
                ppmmics.append(linea[lon:a])"""


import json
import random
from tkinter.ttk import Separator
from turtle import end_fill
import serial
import re
i=1
r=0
lon=0
temperatura=[]
humedad=[]
ppmmq=[]
ppmmics=[]

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
while i!=10:
    linea = ser.readline()
    linea = linea.decode("ANSI")
    i=i+1
    r=0
    a=0
    lon=0
    #linea=linea[1:]
    valores=linea.split('|')
    for j in range(len(valores)):
        valores[j]=re.sub("[^0-9,.,-]", "", valores[j])
    temperatura.append(float(valores[0]))
    humedad.append(float(valores[0]))
    ppmmq.append(float(valores[0]))
    ppmmics.append(float(valores[0]))


dinfo={"temperatura": temperatura,
        "humedad": humedad,
        "ppm-mq": ppmmq,
        "ppm-mics": ppmmics,
}
print(temperatura)
print(linea)
gjson(dinfo)


"""for j in linea:
        a=a+1
        if(j=='|'):
            r=r+1
            if r==1:
                temperatura.append(float(linea[0:a-1]))
                lon=len(linea[0:a])
            elif r==2:
                humedad.append(float(linea[lon:a-1]))
                lon=len(linea[lon:a])
            elif r==3:
                ppmmq.append(linea[lon:a])
                lon=len(linea[lon:a])
            elif r==4:
                ppmmics.append(linea[lon:a])"""