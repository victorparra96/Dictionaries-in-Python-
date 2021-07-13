"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en
un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del
cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un
cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente,
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes,
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6. Terminar el programa.
"""

data = {}

def create_dict(cc:int, name:str, address:str, phone:str, mail:str, preferential:bool):
    data.update({cc: {'name': name, 'address': address, 'phone': phone, 'mail': mail, 'preferential': preferential}})
    return data

def remove_client(cc):
    if cc in data:
        data.pop(cc)
        print("{} \n".format(data))
    else:
        print("The identification {} not exists \n".format(cc))

def show_client(cc):
    if cc in data:
        for clave, valor in data[cc].items():
            print(clave.title() + ':', valor)
    else:
        print("The identification {} not exists \n".format(cc))

def show_all_client():
    for clave, valor in data.items():
        print(clave, valor['name'])

def show_preferential() -> str:
    """ mensaje = ""
    for key, value in data.items():
        for i in value:
            if value[i] == True:
                mensaje += "{} {} \n".format(value['name'], key)
    if mensaje == "":
        mensaje = "Database is empty \n"
    return mensaje """
    for clave, valor in data.items():
        if valor['preferential']:
            print(clave, valor['name'])

if __name__ == '__main__':
    next = True
    while next:
        iterador = input("Ingrese alguna de las opciones \n (1) Añadir cliente \n"
                        " (2) Eliminar cliente \n (3) Mostrar cliente \n (4) Listar todos los clientes \n" 
                        " (5) Listar clientes preferentes \n (6) Terminar \n")
        if iterador == '1':
            cc = input("Enter your identification ").strip()
            name = str(input("Enter your name ").lower().strip())
            address = str(input("Enter your address ").lower().strip())
            phone = str(input("Enter your number phone ").strip())
            mail = str(input("Enter your email ").lower().strip())
            preferential = str(input("You are preferential S/N ").lower().strip())
            if preferential == 's':
                preferential = True
            elif preferential == 'n':
                preferential = False
            if cc.isdigit():
                create_dict(cc, name, address, phone, mail, preferential)
            else:
                print("Enter only numbers, try again")
        elif iterador == '2':
            cc = input("Enter a identification for remove ").strip()
            remove_client(cc)
        elif iterador == '3':
            cc = input("Enter a identification for search ").strip()
            show_client(cc)
        elif iterador == '4':
            show_all_client()
        elif iterador == '5':
            show_preferential()
        else:
            next = False