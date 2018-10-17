def code(invoerstring):
    uitvoerstring = ""
    for teken in invoerstring:
        uitvoerstring += chr(ord(teken) + 3)
    return uitvoerstring


naam = input("Naam: ")
beginstation = input("Beginstation: ")
eindstation = input("Eindstation: ")
invoerstring = naam + beginstation + eindstation

print('Code: ' + code(invoerstring))
