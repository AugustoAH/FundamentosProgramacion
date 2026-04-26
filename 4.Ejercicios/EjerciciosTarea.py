'''
Nivel 1: Calentamiento (Variables y Condicionales Simples)

Estos ejercicios buscan que el estudiante se familiarice con la captura de datos (input), conversión de tipos y condicionales básicos.

1. El saludo personalizado
Enunciado: Pide al usuario su nombre y su edad. Muestra un mensaje de bienvenida y calcula en qué año nació aproximadamente 
(restando la edad al año actual)
Conceptos: Variables, entrada/salida de datos, operaciones matemáticas básicas.
'''
print("Ejercicio 1: El saludo personalizado")
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
año_actual = 2026
año_nacimiento = año_actual - edad
print(f"¡Hola, {nombre}! Naciste aproximadamente en {año_nacimiento}.")
'''
2. Par o Impar
Enunciado: Escribe un programa que pida al usuario un número entero y le diga si es par o impar.
Conceptos: Operador módulo (%), condicional if-else.
'''
print("\nEjercicio 2: Par o Impar")
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
'''

3. El peaje
Enunciado: Pregunta al usuario la edad. Si es mayor o igual a 18 años, muestra el mensaje "Puedes conducir", de lo contrario, muestra "Aún no tienes edad para conducir".
Conceptos: Condicional if-else, operadores relacionales (>=).
'''
print("\nEjercicio 3: El peaje")
edad_conductor = int(input("¿Cuál es tu edad? "))
if edad_conductor >= 18:
    print("Puedes conducir.")
else:
    print("Aún no tienes edad para conducir.")
'''
4. El mayor de dos
Enunciado: Pide al usuario dos números diferentes y muestra por pantalla cuál de los dos es el mayor.
Conceptos: Variables, condicional if-else, comparación (>).
'''
print("\nEjercicio 4: El mayor de dos")
numUno = float(input("Ingresa el primer número: "))
numDos = float(input("Ingresa el segundo número: "))
if numUno > numDos:
    print(f"El número {numUno} es el mayor.")
elif numDos > numUno:
    print(f"El número {numDos} es el mayor.")
else:
    print("Los números son iguales.")
'''
5. Positivo, negativo o cero
Enunciado: Solicita un número al usuario. El programa debe imprimir si el número es positivo, negativo o si es exactamente cero.
Conceptos: Condicionales múltiples (if, elif, else).
'''
print("\nEjercicio 5: Positivo, negativo o cero")
num = float(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
'''
Nivel 2: Lógica Condicional Avanzada

Aquí se introducen múltiples condiciones, operadores lógicos (and, or) y anidamiento.

6. Categoría de edad
Enunciado: Pide la edad al usuario y clasifícalo según las siguientes categorías: 0-12 (Niño), 13-17 (Adolescente), 18-64 (Adulto), 65 o más (Adulto mayor).
Conceptos: Operadores lógicos (and) o anidamiento de elif.
'''
print("\nEjercicio 6: Categoría de edad")
edad_usuario = int(input("¿Cuál es tu edad? "))
if 0 <= edad_usuario <= 12:
    print("Eres un Niño.")
elif 13 <= edad_usuario <= 17:
    print("Eres un Adolescente.")
elif 18 <= edad_usuario <= 64:
    print("Eres un Adulto.")
elif edad_usuario >= 65:
    print("Eres un Adulto mayor.")
else:
    print("Edad no válida.")
'''
7. Descuento en la tienda
Enunciado: Una tienda ofrece descuentos según el monto de la compra. Si es menor a $50, no hay descuento. Si está entre $50 y $100, hay un 5% de descuento. Si es mayor a $100, el descuento es del 10%. Pide el total de la compra y muestra el total a pagar.
Conceptos: Variables, if-elif-else, cálculos de porcentajes.
'''
print("\nEjercicio 7: Descuento en la tienda")
total_compra = float(input("Ingresa el total de tu compra: $"))
if total_compra < 50:
    descuento = 0
elif 50 <= total_compra <= 100:
    descuento = 0.05
else:
    descuento = 0.10
total_a_pagar = total_compra - (total_compra * descuento)
print(f"Total a pagar: ${total_a_pagar:.2f}")
'''
8. Año bisiesto
Enunciado: Pide al usuario que ingrese un año. El programa debe determinar si es bisiesto o no (Un año es bisiesto si es divisible por 4, excepto si es divisible por 100, a menos que también sea divisible por 400).
Conceptos: Operador módulo (%), operadores lógicos anidados (and, or).
'''
print("\nEjercicio 8: Año bisiesto")
anio = int(input("Ingresa un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
'''
9. Calculadora de IMC (Índice de Masa Corporal)
Enunciado: Pide al usuario su peso (en kg) y su altura (en metros). Calcula el IMC (peso/altura^2) y muestra en qué rango se encuentra: Bajo peso (<18.5), Normal (18.5 - 24.9), Sobrepeso (25 - 29.9) u Obesidad (>=30).
Conceptos: Fórmulas matemáticas, if-elif-else.
'''
print("\nEjercicio 9: Calculadora de IMC")
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")       
'''
10. Aprobación de crédito
Enunciado: Pide al usuario su salario mensual y si tiene alguna deuda pendiente (sí/no). Para aprobar el crédito, el salario debe ser mayor a $1000 
y no debe tener deudas. Imprime "Crédito Aprobado" o "Crédito Denegado".
Conceptos: Cadenas de texto en condicionales, operadores lógicos (and).
'''
print("\nEjercicio 10: Aprobación de crédito")
salario = float(input("Ingresa tu salario mensual: $"))
deuda = input("¿Tienes alguna deuda pendiente? (sí/no): ").strip().lower()
if salario > 1000 and deuda == "no":
    print("Crédito Aprobado")
else:
    print("Crédito Denegado")   
'''
Nivel 3: Introducción a los Bucles

En esta sección se trabaja la repetición de tareas con for y while de forma aislada.

11. Cuenta regresiva
Enunciado: Pide al usuario un número entero positivo. Usa un bucle while para mostrar una cuenta regresiva desde ese número hasta 0, y al final 
imprime "¡Despegue!".
Conceptos: Bucle while, decremento de variables.
'''
print("\nEjercicio 11: Cuenta regresiva")
num = int(input("Ingresa un número entero positivo: "))
while num >= 0:
    print(num)
    num -= 1
print("¡Despegue!") 
'''
12. Suma de los primeros N números
Enunciado: Solicita un número N. Usa un bucle for para sumar todos los números desde el 1 hasta N y muestra el resultado final.
Conceptos: Bucle for con range(), variable acumuladora.
'''
print("\nEjercicio 12: Suma de los primeros N números")
N = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(1, N + 1):
    print(f"Sumando : {i} + {suma} = {suma + i}")
    suma += i
print(f"La suma de los primeros {N} números es: {suma}")
'''
13. La tabla de multiplicar
Enunciado: Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 utilizando un bucle for.
Conceptos: Bucle for, formato de cadenas (f-strings).
'''
print("\nEjercicio 13: La tabla de multiplicar")
numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}") 
'''
14. Adivina el PIN
Enunciado: Define una variable con un PIN secreto (ej. "1234"). Usa un bucle while para pedirle al usuario que ingrese el PIN. El programa no debe dejarlo avanzar hasta que ingrese el PIN correcto.
Conceptos: Bucle while, comparación de cadenas.
'''
print("\nEjercicio 14: Adivina el PIN")
pin_secreto = "1234"
while True:
    pin_ingresado = input("Ingresa el PIN: ")
    if pin_ingresado == pin_secreto:
        print("PIN correcto. Acceso concedido.")
        break
    else:
        print("PIN incorrecto. Intenta de nuevo.")
'''
15. Contador de vocales
Enunciado: Pide al usuario que ingrese una frase. Utiliza un bucle for para recorrer cada letra de la frase y cuenta cuántas vocales (a, e, i, o, u) tiene. Imprime el total.
Conceptos: Bucle for sobre una cadena (string), condicionales dentro de un bucle, variable contador.
'''
print("\nEjercicio 15: Contador de vocales")
frase = input("Ingresa una frase: ")
contador_vocales = 0
for letra in frase:
    if letra.lower() in "aeiou":
        contador_vocales += 1
print(f"La frase tiene {contador_vocales} vocales.")
'''
Nivel 4: Integración y Resolución de Problemas (Retos)

Ejercicios que combinan todo: variables, condicionales lógicos y bucles.

16. Adivina el número (con intentos)
Enunciado: El programa define un número secreto entre 1 y 20. El usuario tiene 5 intentos para adivinarlo (usando un bucle while o for). En cada intento, el programa debe decirle si el número ingresado es mayor o menor al número secreto. Si acierta, el bucle se detiene.
Conceptos: Bucle con límite, if-elif-else, interrupción de bucles (break).
'''
print("\nEjercicio 16: Adivina el número")
import random
numero_secreto = random.randint(1, 20)
intentos = 5
print("¡Bienvenido al juego de adivinar el número!")
for intento in range(1, intentos + 1):
    adivinanza = int(input(f"Intento {intento} de {intentos}. Ingresa un número entre 1 y 20: "))
    if adivinanza < numero_secreto:
        print("Demasiado bajo.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intento} intentos.")
        break
else:
    print(f"Lo siento, no adivinaste el número secreto. Era {numero_secreto}.")
'''
17. Validador de números primos
Enunciado: Pide un número al usuario y determina si es primo (solo divisible por 1 y por sí mismo). Usa un bucle para intentar dividir el número por todos los números anteriores a él y un condicional para verificar el residuo.
Conceptos: Bucle for, operador módulo (%), uso de variables booleanas (banderas/flags).
'''
print("\nEjercicio 17: Validador de números primos")
numero = int(input("Ingresa un número entero positivo: "))
if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
'''
18. Cajero Automático Básico
Enunciado: Simula un cajero. El saldo inicial es $1000. Usa un bucle while para mostrar un menú con tres opciones: 
1. Consultar saldo
2. Retirar dinero
3. Ingresar dinero
4. Salir. 
Si el usuario elige retirar, verifica que la cantidad sea menor o igual al saldo disponible antes de restar. El bucle termina solo cuando elige "Salir".
Conceptos: Menús interactivos con while, condicionales anidados, actualización de variables.
'''
print("\nEjercicio 18: Cajero Automático Básico")
saldo = 1000
while True:
    print("================================")
    print("   MENÚ DEL CAJERO AUTOMÁTICO")
    print("================================")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    print("--------------------------------")
    opcion = input("Elige una opción (1, 2, 3 o 4): ")
    
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")
    elif opcion == "2":
        cantidad = float(input("¿Cuánto dinero deseas retirar? $"))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Tu nuevo saldo es: ${saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == "3":
        cantidad = float(input("¿Cuánto dinero deseas ingresar? $"))
        saldo += cantidad
        print(f"Has ingresado ${cantidad:.2f}. Tu nuevo saldo es: ${saldo:.2f}")
    elif opcion == "4":     
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")
'''
19. La caja registradora
Enunciado: Crea un programa que permita al usuario ingresar los precios de varios productos uno por uno. El programa debe seguir pidiendo precios 
usando un while hasta que el usuario ingrese un "0" para indicar que terminó. 
Al finalizar, si el total de la compra supera los $100, aplica un 10% de descuento. Muestra el total a pagar.
Conceptos: Bucle while con condición de salida, acumuladores, condicional al final.
'''
print("\nEjercicio 19: La caja registradora")
# Inicializamos el acumulador del total
total = 0
print("--- Caja Registradora ---")
print("Introduce los precios de los productos (Escribe 0 para terminar):")
# Bucle while con condición de salida
while True:
    precio = float(input("Precio del producto: $"))
    # Condición para romper el bucle
    if precio == 0:
        break
    # Acumulamos el valor
    total += precio
# Aplicamos el descuento si el total supera los $100
if total > 100:
    descuento = total * 0.10
    total_final = total - descuento
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Descuento aplicado (10%): -${descuento:.2f}")
else:
    total_final = total
    print(f"\nSubtotal: ${total:.2f}")
    print("No se aplicó descuento (compra menor o igual a $100).")
# Resultado final
print(f"Total a pagar: ${total_final:.2f}")
'''
20. Sucesión de Fibonacci
Enunciado: Pide al usuario cuántos términos de la sucesión de Fibonacci quiere generar. La sucesión comienza con 0 y 1, y 
cada número siguiente es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8...). Usa un bucle for para calcular y mostrar la serie.
Conceptos: Intercambio de variables temporales, lógica algorítmica, bucle for.
'''
print ("\nEjercicio 20: Sucesión de Fibonacci")
# Pedimos al usuario la cantidad de términos
n = int(input("¿Cuántos términos de la sucesión de Fibonacci quieres ver? "))
# Inicializamos los dos primeros términos
a = 0
b = 1
print("Sucesión de Fibonacci:")
for i in range(n):
    print(a, end=" ")
    
    # Lógica de intercambio:
    # Calculamos el siguiente sumando los dos actuales
    # y actualizamos los valores para la próxima vuelta.
    suma = a + b
    a = b
    b = sum

    