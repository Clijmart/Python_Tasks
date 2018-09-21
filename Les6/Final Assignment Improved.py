def inputLeeftijd():
    leeftijd = int(input('Geef je leeftijd: '))
    return leeftijd

def inputWeekend():
    weekendrit = input('Reis je in het weekend? (Ja/Nee): ').lower()
    if(weekendrit == 'ja'):
        weekendrit = True
    else:
        weekendrit = False
    return weekendrit

def inputAfstandKM():
    afstandKM = int(input('Hoeveel kilometer reis je? \nAfstand: '))
    return afstandKM

def standaardtarief(afstandKM):
    if(afstandKM <= 50):
        if(afstandKM < 0):
            standaardTarief = 0
        else:
            # 50- KM, 0.80 per KM
            standaardTarief = afstandKM * prijs80cent
    else:
        # 50+ KM, vaste prijs van €15 + 0.60 per KM
        standaardTarief = afstandKM * prijs60cent + vastePrijs
    return standaardTarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardTarief = standaardtarief(afstandKM)
    if(weekendrit):
        if(leeftijd < 12 or leeftijd >= 65):
            # Weekendtarief voor <12 en 65+, 35% korting
            ritprijs = standaardTarief * korting35procent
        else:
            # Weekendtarief voor de rest, 40% korting
            ritprijs = standaardTarief * korting40procent
    else:
        if(leeftijd < 12 or leeftijd >= 65):
            # Weekdagtarief voor <12 en 65+, 30% korting
            ritprijs = standaardTarief * korting30procent
        else:
            # Weekdagtarief voor de rest, geen korting
            ritprijs = standaardTarief
    return ritprijs

vastePrijs = 15
korting40procent = 0.60
korting35procent = 0.65
korting30procent = 0.70
prijs80cent = 0.80
prijs60cent = 0.60

leeftijd = inputLeeftijd()
weekendrit = inputWeekend()
afstandKM = inputAfstandKM()

print('De ritprijs is €' + str(round(ritprijs(leeftijd, weekendrit, afstandKM), 2)))