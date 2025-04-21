def solution(s):
    result = []  # Lista para construir el resultado
    
    for char in s:  # Recorremos cada carácter del string
        if char.isupper():  # Si el carácter es mayúscula...
            result.append(' ')  # Añadimos un espacio ANTES de la mayúscula
        result.append(char)  # Añadimos el carácter actual
    
    return ''.join(result)  # Unimos la lista en un string