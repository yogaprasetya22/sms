from cba import c


def panggil():
    strfile = input("Nama File: ")
    strfile = strfile + ".txt"
    return strfile


def soal():
    file = panggil()
    file = open(file, "a")
    nom = input('convert: ')
    nom = nom.replace('-', '')
    nom = nom.replace(' ', '')
    nom = nom.replace(',', '')
    nom = nom.replace('+62', '\n')
    strmasuk = nom
    file.write(strmasuk)
    print(strmasuk)
    file.close()


soal()
