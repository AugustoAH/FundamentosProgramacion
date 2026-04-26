'''
</>  Reto código

Objetivo: Crear un programa que utilice un bucle while para sumar números hasta alcanzar un valor objetivo

Escribe un programa que sume números enteros positivos ingresados por el usuario hasta alcanzar o superar un valor objetivo de 100. El programa debe:

1. Inicializar una variable suma en 0 para llevar el registro de la suma acumulada
2. Utilizar un bucle while que se ejecute mientras la suma sea menor que 100
3. Dentro del bucle, solicitar al usuario que ingrese un número entero positivo
4. Si el usuario ingresa un valor no numérico o un número negativo, mostrar un mensaje de error y continuar solicitando un nuevo número sin añadirlo 
a la suma
5. Si el número es válido, añadirlo a la suma acumulada y mostrar el valor actual de la suma
6. Cuando la suma alcance o supere 100, mostrar un mensaje indicando el valor final de la suma y cuántos números válidos fueron ingresados

Puedes comenzar con este esquema:

Solución:

'''
suma = 0
contador = 0
while suma < 100:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Error: El número debe ser positivo. Intente nuevamente.")
            continue
        suma += numero
        contador += 1
        print(f"Suma actual: {suma}")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número entero positivo.")
print(f"¡Felicidades! La suma final es {suma} y se ingresaron {contador} números válidos.")

# Solución alternativa 

# Programa que suma números enteros positivos hasta alcanzar o superar 100
suma = 0
contador = 0
print("Ingresa números enteros positivos hasta alcanzar o superar 100.")
while suma < 100:
    entrada = input(f"Suma actual: {suma}. Ingresa un número entero positivo: ")
    
    try:
        numero = int(entrada)
        if numero <= 0:
            print("Error: Debes ingresar un número entero positivo.")
        else:
            suma += numero
            contador += 1
            print(f"Número válido. Suma acumulada: {suma}")
    except ValueError:
        print("Error: Entrada inválida. Debes ingresar un número entero.")
# Mensaje final
print(f"\n¡Objetivo alcanzado! La suma final es {suma}.")
print(f"Se ingresaron {contador} números válidos para alcanzar el objetivo.")