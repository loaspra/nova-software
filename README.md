# Nova - Software: GUI
Repositorio para almacenar los scripts y assets para la GUI 

## Github: 

 + Hacer una copia local de sus códigos (en una carpeta distinta a la que contenga este repo) prosiacaso
 + Para Alvaro y Manuel: Antes de pushear revisen el [repo](!https://github.com/loaspra/nova-software/edit/master/README.md) para ver si alguien modifico el archivo `servidor-web.py` antes que ustedes. En caso otro haya modificado el archivo, darle un **git pull** primero. Esto evitará sobreescribir los cambios del otro.
 + Para Walter: Debes de añadir solo los archivos que uses para tu proceso serial: En vez de  **git add .** seria algo como **git add proceso-serial.py**. 

## Requerimientos

Las librerias necesarias son las siguientes

 + Pandas
 + Dash
 + plotly
 + Pyserial
 + Redis     (solo para la conexión entre proceso-serial y servidor-web)

Para instalarlas, correr esto en cmd

```bash
pip install -r requirements.txt
```

---

22/12/2022

### Temas tratados:
 - Formato de los datos (trama de datos)
 - Redis como storage de datos
 - Lectura de los datos del dataframe
 - Estructura de los graficos

### Tareas: 
 - Manuel: Insertar el codigo que grafica un mapa con varios puntos (estaticos)
 - Walter: Modificar codigo para que entrege el formato mencionado (diccionario tipo)
{
        "temperatura": [23.323, 20.32323 ...],
        "humedad": [89.32 88.323 ...],
        "ppm-mq": [113.32 101.32 ...],
        "ppm-mics": [40.36, 54.54 ...],
}

Palero: Diseñar el layout y crear todos los graficos (graficos finos)
Santiago: Integrar los códigos finales
---

## 10/12/2022

### Tareas:

`Walter` --> Revisar archivo proceso-serial.py (cuando puedas subes al repo el que estabas haciendo)

`Alvaro` --> Crear los graficos de temperatura y humedad

`Manuel` --> Extraer el codigo del [repo](!https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-uber-rides-demo) que grafica el maps (solo el codigo indispensable)

`Santiago` > Conectar el Puerto serial con el servidor y definir el dataframe de todos los datos

### Cambios generales:

1. Después de la reu que tuvimos con Marko, decidí usar como intermediario entre el proceso serial y el Dash a un servidor Redis.

    > *esto solo afecta a mi tarea (conectar el proceso serial con el servidor-web)*

    El script de Walter será el producer (el que escribe los datos en redis) y el servidor-web el consumer (el que pide los datos)

2. La trama de datos tendrá que ser proceada y guardada en el server de redis, en vez de mandarla por post al servidor flask.


---


## 26/10/2022

Como quedamos en la reunion, las partes se dividieron asi

### Proceso Serial
 + Daniel
 + Walter

### Servidor Web
 + Alvaro
 + Manuel
 + Santiago

Las instrucciones estan en el archivo respectivo.

El viernes estaremos programando una reu presencial para ver los avances.

--- 
