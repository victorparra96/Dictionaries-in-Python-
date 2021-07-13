"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en
formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
data = {'01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril', '05': 'mayo', '06': 'junio', '07': 'julio',
        '08': 'agosto', '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'}

def show_date(date:str) -> str:
    # day, month, year = date[0:2], date[3:5], date[6:10]
    date = date.split('/')
    if date[1] in data:
        return "Dia {} del mes {} del año {}".format(date[0], data[date[1]], date[2])
    else:
        return "This month is not registered, try now"

if __name__ == '__main__':
    date = str(input("Enter a date in this format dd/mm/yyyy "))
    try:
        if len(date) == 10 and date[2] == '/' and date[5] == '/':
            print(show_date(date))
        else:
            raise Exception("Not date valid")
    except Exception as e:
        print(e)