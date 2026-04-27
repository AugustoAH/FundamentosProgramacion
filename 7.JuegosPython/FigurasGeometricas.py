'''
Enunciado del Ejercicio: Geometría con Bucles (Arte ASCII)

Objetivo: Desarrollar la lógica de programación y el manejo de bucles anidados (for o while) para representar figuras 
geométricas bidimensionales en la terminal utilizando caracteres (como *, + o #).

Descripción de la Tarea

Debes crear un programa que, al ejecutarse, imprima de forma clara las siguientes cinco figuras. El usuario debería poder 
definir el tamaño (lado, radio o altura) de las figuras antes de imprimirlas.

Figuras Requeridas:
	1.	Triángulo Rectángulo: El programa debe imprimir un triángulo alineado a la izquierda.
	2.	Cuadrado: Una representación con la misma cantidad de filas y columnas.
	3.	Rectángulo: Donde la base sea visiblemente mayor a la altura (ejemplo: proporción 2:1).
	4.	Círculo: (Reto de lógica) Utiliza la ecuación del círculo o una aproximación de distancia de puntos para dibujar 
        una forma redondeada.
	5.	Pentágono: Una figura de 5 lados (puedes combinar un triángulo sobre un trapecio o rectángulo).

Requerimientos Técnicos
•	Visualización: Crear un menú que permita elegir la figura a imprimir.
•	Interactividad: El programa debe preguntar al usuario: "Ingrese el tamaño para sus figuras:".
•	Estructura: Utiliza bucles anidados. El bucle externo controlará las filas (eje Y y el interno las columnas (eje X).
•	Presentación: Cada figura debe estar separada por un título y un espacio en blanco para que sea legible.

Ejemplo de Salida Esperada (Tamaño 5)

--- CUADRADO ---
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

--- RECTÁNGULO (5x10) ---
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #

--- TRIÁNGULO ---
# 
# # 
# # # 
# # # # 
# # # # #

--- CÍRCULO (Radio 5) ---
      # # # #      
    # # # # # #    
  # # # # # # # #  
  # # # # # # # #  
    # # # # # #    
      # # # #      

--- PENTÁGONO ---
      #      
    # # #    
  # # # # #  
  # # # # #  
  # # # # #  

  Solución del Ejercicio Propuesto 
'''