'''
</>  Reto código

Objetivo: Crear un programa que extraiga información específica de una cadena de texto

Crea una función llamada extraer_info que reciba como parámetro una cadena de texto representando un correo electrónico con el formato nombre@dominio.extensión. La función debe devolver un diccionario con tres claves:

* nombre_usuario: la parte del correo antes del símbolo @
* dominio: la parte entre @ y el último punto
* extensión: la parte después del último punto

Por ejemplo, si la entrada es "usuario@ejemplo.com", la función debe devolver:

{
    "nombre_usuario": "usuario",
    "dominio": "ejemplo",
    "extension": "com"
}

Si la cadena no contiene el símbolo @ o no tiene extensión (un punto después del @), la función debe devolver un diccionario vacío.

Utiliza los métodos de cadenas y técnicas de slicing que has aprendido para resolver este ejercicio.
'''
# Función para extraer información de un correo electrónico
def extraer_info(correo):
    # Verificar si el correo contiene el símbolo @
    if '@' not in correo:
        return {}
    
    # Dividir el correo en nombre de usuario y dominio
    partes = correo.split('@')
    nombre_usuario = partes[0]
    
    # Verificar si el dominio contiene un punto para la extensión
    if '.' not in partes[1]:
        return {}
    
    # Dividir el dominio para obtener el dominio y la extensión
    dominio_partes = partes[1].split('.')
    dominio = '.'.join(dominio_partes[:-1])  # Unir todas las partes excepto la última para el dominio
    extension = dominio_partes[-1]  # La última parte es la extensión
    
    # Devolver el diccionario con la información extraída
    return {
        "nombre_usuario": nombre_usuario,
        "dominio": dominio,
        "extension": extension
    }
# Ejemplo de uso
correo = "usuario@ejemplo.com"
info = extraer_info(correo)
print(info)

# Otras Solucion posibles:

def extraer_info(correo):
    """
    Extrae información de un correo electrónico con formato nombre@dominio.extension
    
    Args:
        correo (str): Cadena de texto con el correo electrónico
        
    Returns:
        dict: Diccionario con nombre_usuario, dominio y extension, o diccionario vacío si el formato es inválido
    """
    # Verificar si el correo contiene el símbolo @
    if '@' not in correo:
        return {}
    
    # Dividir el correo en la parte del nombre y la parte del dominio+extensión
    nombre_usuario, dominio_completo = correo.split('@', 1)
    
    # Verificar si hay un punto después del @ (para la extensión)
    if '.' not in dominio_completo:
        return {}
    
    # Obtener el dominio y la extensión
    # Usamos el último punto para separar el dominio de la extensión
    dominio, extension = dominio_completo.rsplit('.', 1)
    
    # Crear y devolver el diccionario con la información
    return {
        "nombre_usuario": nombre_usuario,
        "dominio": dominio,
        "extension": extension
    }
# Ejemplos de uso
if __name__ == "__main__":
    print(extraer_info("usuario@ejemplo.com"))
    print(extraer_info("nombre.apellido@subdominio.dominio.org"))
    print(extraer_info("correo_sin_arroba.com"))
    print(extraer_info("usuario@dominiosinpunto"))