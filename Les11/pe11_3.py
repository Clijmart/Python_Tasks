import csv

bestand = 'gamers.csv'
highscore = 0

with open(bestand, 'r') as gamersFile:
    reader = csv.reader(gamersFile, delimiter=';')
    for row in reader:
        if int(row[2]) > highscore:
            highscore = int(row[2])
            date = row[1]
            name = row[0]

    print('De hoogste score is: {} op {} behaald door {}'.format(highscore, date, name))