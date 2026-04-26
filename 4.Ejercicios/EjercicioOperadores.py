'''
</>  Reto código

Objetivo: Crea una calculadora básica que utilice operadores aritméticos para realizar operaciones matemáticas.

Crea una calculadora básica que realice las cuatro operaciones aritméticas fundamentales (suma, resta, multiplicación y división) entre dos números.

Debes solicitar al usuario que introduzca dos números y luego mostrar el resultado de las cuatro operaciones con estos números.

Para cada operación, muestra el resultado con el siguiente formato:

    "La suma de X y Y es: Z"
    "La resta de X y Y es: Z"
    "La multiplicación de X y Y es: Z"
    "La división de X y Y es: Z"

Recuerda manejar el caso especial de división por cero mostrando un mensaje apropiado.

Pista: Utiliza los operadores +, -, *, / y controla la división por cero con una estructura condicional.

        Solución:
'''
# Solicitar al usuario que introduzca dos números
numUno = float(input("Introduce el primer número: "))
numDos = float(input("Introduce el segundo número: "))

# Realizar las operaciones aritméticas
suma = numUno + numDos
resta = numUno - numDos
multiplicacion = numUno * numDos    
# Manejar la división por cero
if numDos != 0:
    division = numUno / numDos
else:
    division = "No se puede dividir por cero"   

# Mostrar los resultados
print(f"La suma de {numUno} y {numDos} es: {suma}")
print(f"La resta de {numUno} y {numDos} es: {resta}")
print(f"La multiplicación de {numUno} y {numDos} es: {multiplicacion}")
print(f"La división de {numUno} y {numDos} es: {division}") 

# Otra Solución posible 

# Calculadora básica con las cuatro operaciones aritméticas fundamentales
# Solicitar al usuario que introduzca dos números
print("Calculadora básica")
print("----------------")
try:
    # Capturar los números del usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    # Realizar las operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    # Mostrar resultados de suma, resta y multiplicación
    print(f"\nLa suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    
    # Manejar la división por cero
    if num2 != 0:
        division = num1 / num2
        print(f"La división de {num1} y {num2} es: {division}")
    else:
        print(f"La división de {num1} y {num2} es: Error - No se puede dividir por cero")
        
except ValueError:
    print("Error: Debes introducir números válidos.")
