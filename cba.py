def panggil():
    strfile = input("Nama File: ")
    strfile = strfile + ".txt"
    return strfile


file = panggil()
ojk = open(file, "r")
ojk.readline()
for no in ojk:
    nom = no.replace('\n', '')
    # nom = int(nom, base=10)
    # print(nom)
    if len(nom) <= 10:
        nom = nom.replace(nom, '')
        print(nom)
    else:
        print(nom)
