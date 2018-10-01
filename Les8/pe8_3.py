invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
intLijst = invoer.split('-')
intLijst.sort()

minLijst = intLijst[0]
maxLijst = intLijst[-1]
lengthLijst = len(intLijst)
sumLijst = 0

for getal in intLijst:
    sumLijst += int(getal)

gemiddeldeLijst = sumLijst / lengthLijst

print('Gesorteerde list van ints: ' + str(intLijst))
print('Grootste getal: ' + str(maxLijst) + ' en Kleinste getal: ' + str(minLijst))
print('Aantal getallen: ' + str(lengthLijst) + ' en Som van de getallen: ' + str(sumLijst))
print('Gemiddelde: ' + str(gemiddeldeLijst))
