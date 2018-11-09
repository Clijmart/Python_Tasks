def inlezen_beginstation(stations):
    while True:
        beginstation = input("Wat is je beginstation? ")
        if beginstation == stations[-1]:
            print(beginstation + " is het eindstation.")
            continue
        if beginstation in stations:
            break
        else:
            print("Deze trein komt niet in " + beginstation + ".")
    return beginstation


def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input("Wat is je eindstation? ")
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                break
        print("Deze trein komt niet in " + eindstation + ".")
    return eindstation


def omroepen_reis(stations, beginstation, eindstation):
    indexEind = stations.index(eindstation)
    indexBegin = stations.index(beginstation)

    print("Het beginstation {} is het {}e station in het traject.".format(beginstation, indexBegin + 1))
    print("Het eindstation {} is het {}e station in het traject.".format(eindstation, indexEind + 1))
    print("De afstand bedraagt {} station(s).".format(indexEind - indexBegin))
    print("De prijs van het kaartje is {} euro.".format((indexEind - indexBegin) * 5))

    print("\n")
    print("Jij stapt in de trein in: " + beginstation)
    for stationnummer in range(1, indexEind - indexBegin):
        print(" - " + stations[indexBegin + stationnummer])
    print("Jij stapt uit in: " + eindstation)


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven",
            "Weert", "Roermond", "Sittard", "Maastricht"]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
