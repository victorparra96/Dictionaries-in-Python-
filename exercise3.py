"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario 
por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""
fruts = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}

def buy_frut(fruit:str, kilo:int):
    if fruit in fruts:
        return fruts[fruit] * kilo
    else:
        return "The fruit {} is not register, please try again".format(fruit)

if __name__ == '__main__':
    fruit = str(input("Enter name of the fruit ").lower())
    kilo = int(input("Enter the kilogram "))
    print(buy_frut(fruit, kilo))