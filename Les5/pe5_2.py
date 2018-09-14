leeftijd = int(input('Leeftijd: '))
paspoort = input('Heb je een Nederlands paspoort? (Ja/Nee) ').lower()

if(leeftijd >= 18 and paspoort == 'ja'):
    print('Hieperdepiep, je mag stemmen!')
elif(paspoort != 'ja'):
    print('Je moet een Nederlands paspoort hebben om te stemmen!')
else:
    print('Je moet minimaal 18 jaar zijn om te stemmen!')