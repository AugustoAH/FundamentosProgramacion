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

import math

def imprimir_menu():
    print("\n" + "="*30)
    print("   MENÚ DE FIGURAS GEOMÉTRICAS")
    print("="*30)
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Círculo")
    print("5. Pentágono")
    print("6. Salir")
    print("="*30)

def dibujar_figuras():
    while True:
        imprimir_menu()
        opcion = input("Elija una opción (1-6): ")

        if opcion == "6":
            print("¡Gracias por usar el generador! Saliendo...")
            break

        if opcion in ["1", "2", "3", "4", "5"]:
            try:
                n = int(input("Ingrese el tamaño (base/radio/lado): "))
            except ValueError:
                print("Error: Ingrese un número entero válido.")
                continue

            print("\nResultado:\n")

            # 1. TRIÁNGULO
            if opcion == "1":
                for i in range(1, n + 1):
                    print("* " * i)

            # 2. CUADRADO
            elif opcion == "2":
                for i in range(n):
                    print("* " * n)

            # 3. RECTÁNGULO
            elif opcion == "3":
                for i in range(n):
                    print("* " * (n * 2))

            # 4. CÍRCULO (Lógica de radio y distancia)
            elif opcion == "4":
                radio = n
                for i in range((2 * radio) + 1):
                    for j in range((2 * radio) + 1):
                        # Ecuación del círculo: x^2 + y^2 = r^2
                        distancia = math.sqrt((i - radio)**2 + (j - radio)**2)
                        if distancia < radio + 0.5:
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
                    print()

            # 5. PENTÁGONO (Combinación de Triángulo y Rectángulo)
            elif opcion == "5":
                # Parte superior (Punta)
                for i in range(1, n, 2):
                    espacios = (n - i) // 1
                    print("  " * espacios + "* " * i)
                # Parte inferior (Base)
                for i in range(n // 2):
                    print("* " * n)
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    dibujar_figuras()