'''
Enunciado del Ejercicio: Simulador de Carga de Archivos

Contexto: En el desarrollo de aplicaciones web y de escritorio, es vital informar al usuario sobre el progreso de tareas 
que no son instantáneas, como la subida de un archivo a la nube. Tu objetivo es programar un codigo que simule visualmente 
este proceso en la consola.

Instrucciones

Escribe un programa en Python (o el lenguaje de tu preferencia) que realice las siguientes acciones:

	1.	Entrada de datos:
•	Solicitar al usuario el tamaño total del archivo (en Megabytes).
•	Solicitar al usuario el tiempo total de subida deseado (en segundos).
	2.	Lógica de simulación:
•	El programa debe calcular cuánto tiempo debe pasar para que la barra aumente su progreso (puedes usar intervalos de 1% o 10%).
•	Utilizar un bucle para representar el paso del tiempo y el aumento del porcentaje.
	3.	Interfaz visual (Consola):
•	Mostrar una barra de progreso que se llene dinámicamente usando caracteres (por ejemplo: [##########..........]).
•	Mostrar el porcentaje actual al lado de la barra (ej: 50%).
•	Al finalizar, el programa debe mostrar un mensaje de "Carga Completa" con el tamaño del archivo procesado.

Ejemplo de Salida Esperada
Ingrese el tamaño del archivo (MB): 100
Ingrese el tiempo de carga (segundos): 5

Iniciando subida de 100 MB...
[#####---------------] 25%
[##########----------] 50%
[###############-----] 75%
[####################] 100%

¡Archivo de 100 MB subido con éxito!

Tips de Lógica para el Estudiante (Opcional)
•	Matemática simple: Si el tiempo total es T y quieres actualizar la barra 20 veces (de 5% en 5%), cada pausa debe ser de T/20 segundos.
•	Librerías sugeridas: En Python, puedes usar time.sleep() para las pausas y el carácter especial \r (retorno de carro) para que la barra se actualice en la misma línea en lugar de imprimir una nueva cada vez.

Solución del Ejercicio Propuesto 

#Solución Uno
import time
import sys

# 1. Entrada de datos
# Usamos un try/except para que el programa no se rompa si escriben letras
try:
    tamano = float(input("Ingrese el tamaño del archivo (MB): "))
    tiempo_total = float(input("Ingrese el tiempo de carga (segundos): "))
except ValueError:
    print("Error: Por favor, ingrese solo números.")
    sys.exit() # Cerramos el programa si hay un error en los datos

print(f"\nIniciando subida de {tamano} MB...")

# 2. Configuración de la barra
pasos = 20  # La barra tendrá 20 segmentos de largo
intervalo_tiempo = tiempo_total / pasos

# 3. Bucle para animar la carga
for i in range(pasos + 1):
    # Calculamos el porcentaje actual (de 0 a 100)
    porcentaje = int((i / pasos) * 100)
    
    # Creamos el dibujo de la barra
    bloques = "#" * i
    espacios = "-" * (pasos - i)
    
    # Imprimimos sin saltar de línea
    # \r hace que el texto se escriba siempre al inicio de la misma línea
    sys.stdout.write(f"\r[{bloques}{espacios}] {porcentaje}%")
    sys.stdout.flush() # Obligamos a la terminal a mostrar el cambio ahora mismo
    
    # Pausamos el programa un breve momento antes de la siguiente iteración
    time.sleep(intervalo_tiempo)

# 4. Mensaje final
print(f"\n\n¡Archivo de {tamano} MB subido con éxito!")
print("="*40)
'''

#Solución Dos

import time
import sys

def formatear_mb(valor):
    if valor.is_integer():
        return str(int(valor))
    return f"{valor:.1f}"

# 1. Entrada de datos
# Usamos un try/except para que el programa no se rompa si escriben letras
try:
    tamano = float(input("Ingrese el tamaño del archivo (MB): "))
    tiempo_total = float(input("Ingrese el tiempo de carga (segundos): "))
except ValueError:
    print("Error: Por favor, ingrese solo números.")
    sys.exit() # Cerramos el programa si hay un error en los datos

if tamano <= 0 or tiempo_total <= 0:
    print("Error: El tamaño y el tiempo deben ser mayores que cero.")
    sys.exit()

tamano_texto = formatear_mb(tamano)

print("\n" + "=" * 60)
print("SIMULADOR DE CARGA DE ARCHIVOS")
print("=" * 60)
print(f"Archivo seleccionado : {tamano_texto} MB")
print(f"Duracion estimada    : {tiempo_total:.1f} segundos")
print("Estado               : Iniciando carga...\n")

# 2. Configuración de la barra
pasos = 30  # La barra tendrá 30 segmentos de largo para verse mejor
intervalo_tiempo = tiempo_total / pasos
animacion = ["|", "/", "-", "\\"]

# 3. Bucle para animar la carga
for i in range(pasos + 1):
    # Calculamos el porcentaje actual (de 0 a 100)
    porcentaje = int((i / pasos) * 100)
    cargado = (tamano * i) / pasos
    
    # Creamos el dibujo de la barra
    if i == pasos:
        barra = "=" * pasos
    else:
        barra = "=" * i + ">>" + "." * (pasos - i - 1)
    icono = animacion[i % len(animacion)]
    
    # Imprimimos sin saltar de línea
    # sys.stdout.write() permite escribir texto sin añadir saltos de línea automáticos ni espacios entre argumentos.
    # sys.stdout.flush() obliga a vaciar ese búfer, asegurando que la salida aparezca instantáneamente en pantalla.
    # \r hace que el texto se escriba siempre al inicio de la misma línea
    sys.stdout.write(
        f"\r{icono} [{barra}] {porcentaje:>3}% | "
        f"{cargado:>6.1f}/{tamano:>6.1f} MB"
    )
    sys.stdout.flush() # Obligamos a la terminal a mostrar el cambio ahora mismo
    
    # Pausamos el programa un breve momento antes de la siguiente iteración
    if i < pasos:
        time.sleep(intervalo_tiempo)

# 4. Mensaje final
print("\n")
print("=" * 60)
print(f"Carga completa: {tamano_texto} MB subidos con exito.")
print("=" * 60)



