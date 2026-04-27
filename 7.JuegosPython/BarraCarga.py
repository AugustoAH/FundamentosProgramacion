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
'''




