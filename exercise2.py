"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
teléfono es <teléfono>.
"""
def show_data(name:str, age:int, address:str, number_phone:int) -> str:
    data = {'name': name, 'age': age, 'address': address, 'number_phone': number_phone}
    return "{} tiene una edad de {} años, vive en {} y su numero de telefono es {}".format(
        data['name'], data['age'], data['address'], data['number_phone'])

if __name__ == '__main__':
    name = str(input("Enter your name ").lower())
    age = int(input("Enter your age "))
    address = str(input("Enter your address ").lower())
    number_phone = int(input("Enter your phone number "))
    print(show_data(name, age, address, number_phone))