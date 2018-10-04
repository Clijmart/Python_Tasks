getalLijst = []
getal = 1

while getal != 0:
    getal = int(input('Geef een getal: '))
    getalLijst.append(getal)

print('Er zijn ' + str(len(getalLijst) - 1) + ' getallen ingevoerd, de som is: ' + str(sum(getalLijst)))
