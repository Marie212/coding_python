import os
import csv
import shutil

lista =[]
FILE_NAME = ('students.csv')
with open(FILE_NAME) as data:
    next(data)
    entrada = csv.reader(data)
    lista=list(entrada)
    indice = 1
for linea in lista:
    name = str(linea)
    string = name
    characters = "[',0123456789]"
    for x in range(len(characters)):
        string = string.replace(characters[x],"")
    names_doc = str(indice) + '.' + string
    indice += 1
    os.mkdir(str(names_doc))   #modulo para usar el sistema operativo

if __name__ == "__main__":
    for (root, dirs, files) in os.walk('.', topdown = True):
        for x in files:
            if x.endswith(".pdf"):
                shutil.move(f'data/{x}', '16.Tutorials')
        for y in dirs:
            if 'game' in y:
                shutil.move(f'data/{y}', '15.Games')