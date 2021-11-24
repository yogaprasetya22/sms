from cba import c


def panggil():
    strfile = input(c.ly+"Nama File: ")
    strfile = strfile + ".txt"
    return strfile


def soal():
    file = panggil()
    file = open(file, "a")
    nom = input('convert: ')
    nom = nom.replace(',', '\n')
    strmasuk = nom
    file.write(strmasuk)
    print(strmasuk)
    file.close()
    print(file)


soal()
