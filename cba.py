import time


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
        no = nom.replace(nom, '89999999999')
        print(no+' mmk')
    elif len(nom) >= 10:
        print(nom)

