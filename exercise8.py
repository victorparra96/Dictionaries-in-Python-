"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en
español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el
diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

translate = {}

def create_dict(key, data):
    translate.update({key: data})
    return translate

def show_data(data) -> str:
    mensaje = ""
    for i in data.split():
        if i in translate:
            mensaje += "{} ".format(translate[i])
        else:
            mensaje += "{} ".format(i)
    return mensaje

if __name__ == '__main__':
    next = True
    while next:
        data = str(input("Enter a word and it's translation <palabra>:<traducción> ").lower().strip())
        data = data.split(':')
        create_dict(data[0], data[1])
        current = input("Desea seguir agrengando datos. S/N ").lower()
        if current == 'n':
            next = False
    while next == False:
        data = input("Enter a word in spanish for search the translate ").lower().strip()
        print(show_data(data))
        current = input("Desea seguir buscando palabras. S/N ").lower()
        if current == 'n':
            next = True