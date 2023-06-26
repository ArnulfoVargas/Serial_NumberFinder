"""
Este Proyecto Toma la carpeta de Mi_GranDirectorio, y busca en cada uno de los archivos existentes, numeros seriales
con la siguiente disposicion [N] + [tres carateres de texto] + [-] + [5 números]
"""

import math
import os
import re
import datetime
import time
import pathlib
from collections import namedtuple


def find_serial_data():
    route = "C:\\Users\\PC\\Documents\\CursoPython\\Leccion9\\Scripts\\Extraccion\\Mi_Gran_Directorio"
    serial_format = r'N\w{3}-\d{5}'
    founded = []
    Serial = namedtuple("Serial", ['Archive', 'SerialData'])

    for folder, subfolder, archive in os.walk(route):
        for arch in archive:
            route = pathlib.Path(folder.replace("\\","/" ))
            text = open(route / arch).read()
            found = re.findall(serial_format, text)

            for s in found:
                founded.append(Serial(arch, s))

    return founded


def get_time_and_data():
    t = time.time()
    data = find_serial_data()
    t = time.time() - t;
    return data, t


def print_data(function):
    data, t = function()
    date = datetime.datetime.today().date()

    print(
f"""
{"-" * 36}
Fecha de hoy: {f"{date.day}/{date.month}/{date.year}"}

ARCHIVO\t\t\t\t\tNUMERO DE SERIE
-------\t\t\t\t\t---------------""")
    for i in data:
        print(f"{i.Archive}\t\t\t{i.SerialData}")
    print(
f"""
Numeros encontrados: {len(data)}
Duracion de la busqueda: {math.ceil(t)}
{"-" * 36}""")


print_data(get_time_and_data)
