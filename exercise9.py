"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en
un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa
debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una
nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una
factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa
debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

invoice = {}
total = [0]

def create_dict(num_invoice, invoice_value):
    invoice.update({num_invoice: invoice_value})
    return invoice

def payment_invoice(num_invoice):
    if num_invoice in invoice:
        suma = int(invoice[num_invoice]) + int(total[0])
        total[0] = suma
        invoice.pop(num_invoice)
    else:
        print("Invoice {} not exists, try again".format(num_invoice))

def show_data() -> str:
    suma = sum(invoice.values())
    return "Cantidad cobrada {}, pendiente por cobro {}".format(total[0], suma)

if __name__ == '__main__':
    next = True
    while next:
        iterador = str(input("Que neceitas hacer, Agregar/pagar/Salir. A/P/S ").lower().strip())
        if iterador == 'a':
            num_invoice = str(input("Enter a new invoice ").lower().strip())
            invoice_value = input("Enter a value for the invoice # {} ".format(num_invoice)).strip()
            if invoice_value.isdigit():
                create_dict(num_invoice, int(invoice_value))
                print(show_data())
            else:
                print("Enter only numbers, try again")
        elif iterador == 'p':
            num_invoice = str(input("Enter number of invoice ").lower().strip())
            payment_invoice(num_invoice)
            print(show_data())
        else:
            next = False
            break