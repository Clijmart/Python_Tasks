bedrag = 4356

try:
    aantal = int(input("Hoeveel personen gaan er mee op reis? "))
    if aantal < 0:
        print("Negatieve getallen zijn niet toegestaan!")
    else:
        print(bedrag / (aantal))
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except:
    print("Onjuiste invoer!")