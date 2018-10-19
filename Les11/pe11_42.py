import csv

bestand = 'prijzen.csv'


def duurste_product(bestand):
    hoogstePrijs = 0.0
    duursteProduct = ''
    with open(bestand, 'r') as prijsFile:
        reader = csv.DictReader(prijsFile, delimiter=';')
        for product in reader:
            if float(product['Prijs']) > hoogstePrijs:
                hoogstePrijs = float(product['Prijs'])
                duursteProduct = product['Naam']
        print('Het duurste artikel is {} en die kost {} Euro'.format(duursteProduct, hoogstePrijs))


def kleinste_voorraad(bestand):
    kleinsteVoorraad = -1
    nummerProduct = -1
    with open(bestand, 'r') as prijsFile:
        reader = csv.DictReader(prijsFile, delimiter=';')
        for product in reader:
            if int(product['Voorraad']) < kleinsteVoorraad or kleinsteVoorraad == -1:
                kleinsteVoorraad = int(product['Voorraad'])
                nummerProduct = product['Artikelnummer']
        print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(kleinsteVoorraad, nummerProduct))


def totale_voorraad(bestand):
    totaleVoorraad = 0
    with open(bestand, 'r') as prijsFile:
        reader = csv.DictReader(prijsFile, delimiter=';')
        for product in reader:
            totaleVoorraad += int(product['Voorraad'])
        print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaleVoorraad))


duurste_product(bestand)
kleinste_voorraad(bestand)
totale_voorraad(bestand)
