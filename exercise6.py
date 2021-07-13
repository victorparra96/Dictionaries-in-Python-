"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se
añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

new_dict = {}

def create_dict(key, data):
    new_dict.update({key: data})
    return new_dict

if __name__ == '__main__':
    next = True
    while next:
        key = input("Ingrese un dato como llave ")
        data = input("Ingrese un valor para {} ".format(key))
        print(create_dict(key, data))
        current = input("Desea seguir agrengando datos. S/N ").lower()
        if current == 'n':
            next = False