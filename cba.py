import re


def panggil():
    strfile = input("Nama File: ")
    strfile = strfile + ".txt"
    return strfile

data = []

file = panggil()
ojk = open(file, "r")
ojk.readline()
for no in ojk:
    nom = no.replace('\n', '')
    if len(nom) <= 10:
        no = nom.replace(nom, '00000000000')
        print(no+' mmk')
        # print(nom)
    else:
        print(nom)
