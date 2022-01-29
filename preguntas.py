"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from posixpath import split


original_data = open('data.csv', 'r').readlines()
ezData = [row[0:-1] for row in original_data]
ezData = [row.split() for row in ezData]


def pregunta_01():
    data = [int(row[2]) for row in original_data]
    ans = sum(data)
    return ans


def pregunta_02():
    column_letras = [row[0] for row in ezData]
    letra_aparicion = {i:column_letras.count(i) for i in column_letras}
    ans = list(letra_aparicion.items())
    return sorted(ans)


def pregunta_03():
    cols_tuple = [(row[0], int(row[1])) for row in ezData]
    column_letras = [row[0] for row in ezData]
    letra_aparicion = {i:0 for i in column_letras}
    new_dic = {}
    for letter in letra_aparicion.keys():
        aux = 0
        for element in cols_tuple:
            if (element[0] == letter):
                aux = aux + element[1]
        new_dic[letter] = aux
    ans = list(new_dic.items())
    return sorted(ans)


def pregunta_04():
    column_fechas = [row[2] for row in ezData]
    meses = [letra[5:7] for letra in column_fechas]
    apariciones = {i:meses.count(i) for i in meses}
    ans = list(apariciones.items())
    return sorted(ans)


def pregunta_05():
    cols_tuple = [(row[0], int(row[1])) for row in ezData]
    letras_unicas = set([row[0] for row in ezData])
    aux_list_2 = []
    for letter in letras_unicas:
        aux_list_1 = []
        for element in cols_tuple:
            if (element[0] == letter):
                aux_list_1.append(element[1])
        aux_list_2.append(tuple([letter, max(aux_list_1), min(aux_list_1)]))
    return sorted(aux_list_2)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    col_cadena = [row[4] for row in ezData]
    col_individual = [elemento.split(",") for elemento in col_cadena]
    lista_plana = [i for sublist in col_individual for i in sublist]
    letras = [elemento[0:3] for elemento in lista_plana]
    numeros = [int(elemento[4:]) for elemento in lista_plana]
    cols_tuple = list(zip(letras, numeros))
    letras_unicas = set(letras)
    aux_list_2 = []
    for letter in letras_unicas:
        aux_list_1 = []
        for element in cols_tuple:
            if (element[0] == letter):
                aux_list_1.append(element[1])
        aux_list_2.append(tuple([letter, min(aux_list_1), max(aux_list_1)]))
    return sorted(aux_list_2)


def pregunta_07():
    nums_unicos = set([int(row[1]) for row in ezData])
    cols_tuple = [(row[0], int(row[1])) for row in ezData]
    ans_list = []
    for number in nums_unicos:
        aux_list = []
        for element in cols_tuple:
            if (element[1] == number):
                aux_list.append(element[0])
        ans_list.append(tuple([number, aux_list]))
    return ans_list


def pregunta_08():
    nums_unicos = set([int(row[1]) for row in ezData])
    cols_tuple = [(row[0], int(row[1])) for row in ezData]
    ans_list = []
    for number in nums_unicos:
        aux_list = []
        for element in cols_tuple:
            if (element[1] == number):
                aux_list.append(element[0])
        ans_list.append(tuple([number, sorted(list(set(aux_list)))]))
    return ans_list


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
