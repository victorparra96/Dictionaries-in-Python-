""" 
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
currency = {'euro':'€', 'dollar':'$', 'yen':'¥'}

def choose_currency():
    currency_entered = str(input("Enter one currency ").lower())
    if currency_entered in currency:
        print(f"The currency chosen is {currency_entered} {currency[currency_entered]}")
    else:
        print(f"The currency chosen {currency_entered} is not register, please try again")

if __name__ == '__main__':
    choose_currency()