"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo
y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla
la lista de la compra y el coste total, con el siguiente formato
"""

shop = {}

def create_dict(key, data):
    shop.update({key: data})
    return shop

def show_data() -> str:
    suma = 0
    mensaje = ""
    for key, value in shop.items():
        suma += int(value)
        mensaje += "{} {} \n".format(key, value)
    return mensaje + "Total {}".format(suma)

if __name__ == '__main__':
    next = True
    while next:
        key = str(input("Ingrese el nombre del producto que desea ").lower())
        data = input("Ingrese el precio de {} ".format(key))
        if data.isdigit():
            create_dict(key, data)
        else:
            print("Debes ingresar solo numeros, intenta de nuevo")
        current = input("Desea seguir agrengando datos. S/N ").lower()
        if current == 'n':
            next = False
    print("Lista de compra")
    print(show_data())