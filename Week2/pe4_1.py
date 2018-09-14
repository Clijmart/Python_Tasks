cijferICOR = 1
cijferPROG = 10
cijferCSN = 10

gemiddelde = round((cijferICOR + cijferPROG + cijferCSN) / 3, 1)
beloning = float((cijferICOR + cijferPROG + cijferCSN) * 30)
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van €' + str(beloning) + ' op!'

print(overzicht)