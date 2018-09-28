vastePrijs = 15
leeftijdKorting = 0.65
weekendLeeftijdKorting = 0.70
weekendKorting = 0.60
prijsKorteAfstand = 0.80
prijsLangeAfstand = 0.60
standaardAfstandPrijsVerandering = 50
jeugdTariefLeeftijd = 12
ouderenTariefLeeftijd = 65

def inputLeeftijd():
    leeftijd = int(input('Geef je leeftijd: '))
    return leeftijd

def inputWeekend():
    weekendrit = input('Reis je in het weekend? (Ja/Nee): ').lower()
    return weekendrit == 'ja'

def inputAfstandKM():
    afstandKM = int(input('Hoeveel kilometer reis je? \nAfstand: '))
    return afstandKM

def standaardtarief(afstandKM):
    if(afstandKM <= standaardAfstandPrijsVerandering):
        if(afstandKM < 0):
            standaardTarief = 0
        else:
            # 50- KM, 0.80 per KM
            standaardTarief = afstandKM * prijsKorteAfstand
    else:
        # 50+ KM, vaste prijs van €15 + 0.60 per KM
        standaardTarief = afstandKM * prijsLangeAfstand + vastePrijs
    return standaardTarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardTarief = standaardtarief(afstandKM)
    rechtOpLeeftijdKorting = leeftijd < jeugdTariefLeeftijd or leeftijd >= ouderenTariefLeeftijd
    if(weekendrit):
        if(rechtOpLeeftijdKorting):
            # Weekendtarief voor <12 en 65+, 35% korting
            ritprijs = standaardTarief * leeftijdKorting
        else:
            # Weekendtarief voor de rest, 40% korting
            ritprijs = standaardTarief * weekendKorting
    else:
        if(rechtOpLeeftijdKorting):
            # Weekdagtarief voor <12 en 65+, 30% korting
            ritprijs = standaardTarief * weekendLeeftijdKorting
        else:
            # Weekdagtarief voor de rest, geen korting
            ritprijs = standaardTarief
    return ritprijs


leeftijd = inputLeeftijd()
weekendrit = inputWeekend()
afstandKM = inputAfstandKM()

print('De ritprijs is €' + str(round(ritprijs(leeftijd, weekendrit, afstandKM), 2)))
