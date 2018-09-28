def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    date = vandaag.strftime("%a %d %b %Y")
    return date


hardlopers = open('hardlopers.txt', 'a')

while True:
    name = input('Naam hardloper (Write "Exit" to exit): ')
    if name == 'Exit' or name == 'exit':
        hardlopers.close()
        exit()
    time = input('Tijd hardloper (HH:MM:SS): ')
    hardlopers.write(strftime() + ', ' + time + ', ' + name + '\n')
