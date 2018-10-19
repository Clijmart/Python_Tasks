import datetime
import csv

bestand = 'inloggers.csv'

dateFormat = datetime.date.today().strftime('%a %d %b %Y')
timeFormat = datetime.datetime.now().strftime('%H:%M')
fullDate = '{} at {}'.format(dateFormat, timeFormat)

while True:
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    with open(bestand, 'w') as inloggersFile:
        writer = csv.writer(inloggersFile, delimiter=';')
        writer.writerow((fullDate, voorl, naam, gbdatum, email))
