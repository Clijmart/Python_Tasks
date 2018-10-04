cijfers = {
    'Piet': [5.1, 6.6, 7.2, 8.8],
    'Abe': [9.4, 10.0, 4.2, 6.0],
    'Klaas': [8.4, 9.0]
}
for student in cijfers:
    for cijfer in cijfers[student]:
        if cijfer >= 9.0:
            print(student + ' heeft ' + str(cijfer))
