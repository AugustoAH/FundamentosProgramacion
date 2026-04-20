'''
En programación podemos definir un bucle como la repetición de la ejecución de un conjunto
de instrucciones donde a cada repetición del conjunto de instrucciones se llama iteracción.

Los Bucles están compuestos por los siguientes elementos:
──▶ Punto de inicio: Es el punto donde se inicia la ejecución del bucle.
──▶ Punto de fin: Es el punto donde se detiene la ejecución del bucle.
──▶ Número de iteracciones: Es el número de veces que se ejecutará el conjunto de instrucciones.
──▶ Bloque de instrucciones: Es el conjunto de instrucciones que se ejecutará en cada iteracción del bucle.

Existen dos tipos de bucles:
──▶ Bucle for: Es un bucle que se ejecuta un número determinado de veces. 
               Se utiliza cuando se conoce el número de iteracciones que se van a realizar.

En python los bucles (for) se ejecutan sobre elementos iterables, como listas, tuplas, diccionarios, etc.
El número de iteracciones se determina por el número de elementos en el iterable.

Los bubles (for) tienen la siguiente sintaxis:
for variable in ColeccionIterable:
    bloque de instrucciones

Elementos en detalle:

(for): Indicador de comienzo del bucle for.
(variable): Es la variable que tomará el valor de cada elemento del iterable en cada iteracción.
(in): indicador que se utiliza para definir el elemento iterable sobre el que se va a iterar.
(ColeccionIterable): Es la colección de elementos sobre la que se va a iterar.
(bloque de instrucciones): Es el conjunto de instrucciones que se ejecutará en cada iteracción.

              [Inicio]
                 |
          (for i in lista:)
                 |
┌───▶ [¿Hay siguiente item?] ──────(False)──────┐
│                |                              |
│              (True)                           |
│                ▼                              |
│          [Bloque Código]                      |
│                |                              |
└────────────────┘                              ▼
                                            [ Sigue ]
                                                |
                                              [Fin]
'''
nombres = ["Ana", "Leo", "Mia"] # Lista de nombres
                                 # ┌──▶ [¿Hay más items?] ──(F)──┐
for nombre in nombres:           # │          │                  │
    print(f"Hola {nombre}")      # │         (V)                 │
                                 # │          ▼                  │
                                 # │    [Bloque Código]          │
                                 # └──────────┘                  │
print("Todos saludados")         #                           [ Sigue ]

#----------------------------------------------------------------------
                                     # ┌──▶ [¿Quedan números?] ──(F)──┐
for i in range(1, 6):                # │           │                  │
    print(f"Número: {i}")            # │          (V)                 │
                                     # │           ▼                  │
                                     # │    [Imprimir Número]         │
                                     # └───────────┘                  │
print("Fin del conteo")              #                            [ Sigue ]

'''
──▶ Python (in): La funcion (in) significa "en" su función es decirle a Python que mire dentro de un grupo de cosas 
y saque los elementos uno por uno".

──▶ Python (range): Como a veces no tenemos una lista ya creada, usamos range(), esta función fabrica una secuencia de 
números sobre la marcha, es como una máquina que genera una fila de números para que el (for)
los recorra.

A. range(final)
Si le das un solo número, genera una lista que empieza en 0 y llega hasta uno antes del número que pusiste.
range(5) → 0, 1, 2, 3, 4

B. range(inicio, final)
Tú eliges dónde empezar.
range(5, 10) → 5, 6, 7, 8, 9 (el 10 nunca se incluye).

C. range(inicio, final, salto)
El tercer número es para saltar de tanto en tanto.
range(1, 11, 2) → 1, 3, 5, 7, 9 (va saltando de 2 en 2).


──▶ Bucle while: Es un bucle que se ejecuta mientras se cumpla una condición. 
 Se utiliza cuando no se conoce el número de iteracciones que se van a realizar, 
 pero se sabe que se desea repetir un bloque de instrucciones mientras se cumpla una condición.    

La condición que se utiliza para comprobar si se tiene que ejecutar una
interacción deberá ser (true), la ejecución del bucle se detendrá cuando 
la condición sea (false). La condición se evalúa antes de cada iteracción,
por lo que si la condición es (false) desde el principio, el bloque de instrucciones 
no se ejecutará ni una sola vez.

Los bucles (while) tienen la siguiente sintaxis:
while condición:
    bloque de instrucciones

Elementos en detalle:
(while): Indicador de comienzo del bucle while.
(condición): condición que se debe de cumplir para que siga repitiéndose la ejecución
del bucle.
(bloque de instrucciones): Es el conjunto de instrucciones que se ejecutará en cada iteracción

           [Inicio]
               |
         while x > 0:)
               |
┌──────▶ [¿Condición?] ─────(False)───────┐
│              |                          |
│           (True)                        |
│              ▼                          |
│       [Bloque Código]                   |
│              |                          |
└──────────────┘                          ▼
                                      [ Sigue ]
                                          |
                                        [Fin]           
'''
contador = 3

                                 # ┌──▶ [¿contador > 0?] ──(F)──┐
while contador > 0:              # │           │                │
    print(contador)              # │          (V)               │
    contador -= 1                # │           ▼                │
else:                            # │    [Bloque Código]         │
    print("¡Despegue!")          # └───────────┘                │
                                 #                          [ Sigue ]


