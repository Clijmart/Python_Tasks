def kwadraten_som(grondgetallen):
    output = 0
    for getal in grondgetallen:
        if (getal >= 0):
            output += getal ** 2
    return output


print(kwadraten_som([14, 5, 3, -7, -54115]))
