def standaardtarief(afstandKM):
    if(afstandKM <= 50):
        if(afstandKM < 0):
            return 0
        else:
            # 50- KM, 0.80 per KM
            return afstandKM * 0.80
    else:
        # 50+ KM, vaste prijs van €15 + 0.60 per KM
        return afstandKM * 0.60 + 15

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardTarief = standaardtarief(afstandKM)
    if(weekendrit):
        if(leeftijd < 12 or leeftijd >= 65):
            # Weekendtarief voor <12 en 65+, 35% korting
            return standaardTarief * 0.65
        else:
            # Weekendtarief voor de rest, 40% korting
            return standaardTarief * 0.60
    else:
        if(leeftijd < 12 or leeftijd >= 65):
            # Weekdagtarief voor <12 en 65+, 30% korting
            return standaardTarief * 0.70
        else:
            # Weekdagtarief voor de rest, geen korting
            return standaardTarief


leeftijd = 65
weekendrit = True
afstandKM = 60

print('De ritprijs is €' + str(round(ritprijs(leeftijd, weekendrit, afstandKM), 2)))