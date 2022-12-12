# Nova - Software: GUI
Repositorio para almacenar los scripts y assets para la GUI 

## Requerimientos

Las librerias necesarias son las siguientes

 + Pandas
 + Dash
 + plotly
 + Pyserial

Para instalarlas, correr esto en cmd

```bash
pip install pandas dash plotly pyserial
```

---

## 10/12/2022

### Tareas:

`Walter` --> Revisar archivo proceso-serial.py (cuando puedas subes al repo el que estabas haciendo)

`Alvaro` --> Crear los graficos de temperatura y humedad

`Manuel` --> Extraer el codigo del [repo](!https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-uber-rides-demo) que grafica el maps (solo el codigo indispensable)

`Santiago` > Conectar el Puerto serial con el servidor y definir el dataframe de todos los datos

### Cambios importantes:

1. Después de la reu que tuvimos con Marko, decidí usar como intermediario entre el proceso serial y el Dash a un servidor Redis.

    > *esto solo afecta a mi tarea (conectar el proceso serial con el servidor-web)*

    El script de Walter será el producer (el que escribe los datos en redis) y el servidor-web el consumer (el que pide los datos)

2. 


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