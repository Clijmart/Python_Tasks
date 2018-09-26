kaartnummers = open('kaartnummers.txt')
for i in range(6):
    line = kaartnummers.readline()
    nummer = line[:6]
    naam = line[8:-1]

    print(naam + ' heeft kaartnummer: ' + nummer)
kaartnummers.close()
