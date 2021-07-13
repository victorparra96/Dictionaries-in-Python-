"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en 
el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y 
<créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""

asignature = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

def show_data() -> str:
    data = ""
    suma = 0
    for key, value in asignature.items():
        data += "{} tiene {} creditos, ".format(key, value)
        suma += value
    return data + "el valor total de los creditos es {}".format(suma)

if __name__ == '__main__':
    print(show_data())