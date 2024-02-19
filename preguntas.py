"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from hashlib import new
from operator import le
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
    col_cadena = [row[4] for row in ezData]
    col_individual = [elemento.split(",") for elemento in col_cadena]
    lista_plana = [i for sublist in col_individual for i in sublist]
    letras = sorted([elemento[0:3] for elemento in lista_plana])
    apariciones = {i:letras.count(i) for i in letras}
    return apariciones


def pregunta_10():
    letras = [tuple([row[0], len(row[3].split(",")), len(row[4].split(","))]) for row in ezData]
    return letras


def pregunta_11():
    letras = [row[3] for row in ezData]
    col_individual = [elemento.split(",") for elemento in letras]
    lista_plana_letras = sorted([i for sublist in col_individual for i in sublist])
    lista_nums = []
    lista_letras = []

    for i in range(len(col_individual)):
        for subelems in col_individual[i]:
            lista_nums.append(int(ezData[i][1]))
            lista_letras.append(subelems)
    tup = list(zip(lista_letras, lista_nums))

    letra_aparicion = {i:0 for i in lista_plana_letras}
    new_dic = {}
    for letter in letra_aparicion.keys():
        aux = 0
        for element in tup:
            if (element[0] == letter):
                aux = aux + element[1]
        new_dic[letter] = aux

    return new_dic


def pregunta_12():
    column_letras = [row[0] for row in ezData]
    col_cadena = [row[4] for row in ezData]
    col_individual = [elemento.split(",") for elemento in col_cadena]
    lista_suma = []
    for sublist in col_individual:
        inside_list = []
        for element in sublist:
            inside_list.append(int(element[4:]))
        lista_suma.append(sum(inside_list))
    cols_tuple = list(zip(column_letras, lista_suma))
    
    letra_aparicion = {i:0 for i in sorted(column_letras)}
    new_dic = {}
    for letter in letra_aparicion.keys():
        aux = 0
        for element in cols_tuple:
            if (element[0] == letter):
                aux = aux + element[1]
        new_dic[letter] = aux
    return new_dic