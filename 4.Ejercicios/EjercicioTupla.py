'''
</>  Reto código

Objetivo: Crear y manipular una tupla con información de contactos

Crea una tupla llamada contacto que contenga la siguiente información en este orden: nombre, correo electrónico y número de teléfono. 
Utiliza los valores "Ana García", "ana@ejemplo.com" y "555-1234".

Luego, realiza las siguientes operaciones:

    * Desempaqueta la tupla en tres variables llamadas nombre, email y telefono.
    * Imprime cada variable en líneas separadas.
    * Crea una nueva tupla llamada contacto_completo que contenga los elementos de la tupla original más la ciudad "Madrid" al final.

Recuerda que las tuplas son inmutables, por lo que deberás crear una nueva tupla para añadir el elemento adicional.

            Solución:
'''
# Ejercicio de tuplas en Python
# 1. Crear la tupla contacto con la información requerida
contacto = ("Ana García", "ana@ejemplo.com", "555-1234")
# 2. Desempaquetar la tupla en tres variables
nombre, email, telefono = contacto
# 3. Imprimir cada variable en líneas separadas
print(nombre)
print(email)
print(telefono)
# 4. Crear una nueva tupla con los elementos originales más la ciudad "Madrid"
contacto_completo = contacto + ("Madrid",)
# Mostrar la nueva tupla para verificar
print("\nTupla contacto_completo:")
print(contacto_completo)


'''
La solución cumple correctamente con los pasos solicitados en el enunciado:

    Creas la tupla contacto con tres elementos y en el orden adecuado.
    Desempaquetas la tupla en nombre, email y telefono de forma correcta.
    Imprimes cada variable en una línea distinta con print(...) separados.
    Creas una nueva tupla contacto_completo añadiendo la ciudad "Madrid" al final mediante contacto + ('Madrid',), respetando la inmutabilidad de las tuplas.

Como detalle menor, el correo electrónico tiene un pequeño error tipográfico ('ana@ejmeplo.com' en lugar de 'ana@ejemplo.com'), pero a nivel de programación la solución es totalmente válida.

Buen uso de la sintaxis de tuplas, desempaquetado y concatenación. ¡Buen trabajo!
'''