# Tipos de datos básicos
edad = 21  # edad
altura = 1.75  # altura
nombre = "Juan"  # Un texto

# Convertir un número a texto para que lo pueda imprimir con otras palabras
edad_como_cadena = str(edad)
print("Mi edad es:", edad_como_cadena)  # Aquí ya puedo juntar el número con otras palabras

# Convertir texto a número, solo si el texto es un número válido
numero = int("42")
print("El número es:", numero)  # Ahora "42" ya es un número de verdad

# Cómo escribir varias líneas de texto en una variable
texto_largo = """
Esta es una cadena de múltiples líneas.
Podemos escribir lo que queramos sin preocuparnos por los saltos de línea.
"""
print(texto_largo)  # Aquí imprimo el texto largo tal cual

# Para saber cuántas letras tiene un nombre
longitud_nombre = len(nombre)
print("La longitud del nombre es:", longitud_nombre)  # Me dice cuántas letras tiene "Juan"

# Sacar pedacitos de una frase
frase = "Python es genial"
primeros_cinco = frase[:5]  # Los primeros 5 caracteres
medio = frase[7:12]  # los caracteres del medio de la frase
ultimos_cuatro = frase[-4:]  # Los últimos 4 caracteres
print(primeros_cinco, medio, ultimos_cuatro)  # Imprime

# Poner todo en mayúsculas o minúsculas
frase_mayusculas = frase.upper()  # Todo en mayúsculas
frase_minusculas = frase.lower()  # Todo en minúsculas
print(frase_mayusculas, frase_minusculas)  # Lo imprime

# Quitar los espacios extra que sobran al inicio o al final
cadena_con_espacios = "   Hola, mundo!   "  # Tiene muchos espacios alrededor
cadena_sin_espacios = cadena_con_espacios.strip()  # Le quito los espacios extras
print(cadena_sin_espacios)  # imprime

# Cambiar una palabra de la frase por otra
nueva_frase = frase.replace("genial", "increíble")  # Cambio "genial" por "increíble"
print(nueva_frase)  # Imprime la frase con el cambio

# Separar la frase en palabras
palabras = frase.split()  # Separa la frase en palabras donde haya un espacio
print(palabras)  # Imprime la lista de palabras que salió

# Usar variables dentro de una frase
nombre = "Ana"
edad = 25
saludo = f"Hola, {nombre}. ¡Felicidades por tus {edad} años!"  # Aquí uso las variables directo en el texto
print(saludo)  # Imprime el saludo personalizado
