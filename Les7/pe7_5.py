def gemiddelde(zin):
    zinList = zin.split(' ')

    # Lengte Zin - Spaties / Aantal Woorden
    return (len(zin) - len(zinList) + 1) / len(zinList)


zin = input('Willekeurige zin: ')
print('De gemiddelde lengte van een woord in de zin is ' + str(gemiddelde(zin)) + ' letters.')
