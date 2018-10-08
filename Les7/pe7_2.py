kaartnummers = open('kaartnummers.txt')
lines = kaartnummers.readlines()
kaartnummers.close()
for line in lines:
    nummer = line[:line.index(',')]
    naam = line[line.index(',') + 2:-1]
    print(naam + ' heeft kaartnummer: ' + nummer)
