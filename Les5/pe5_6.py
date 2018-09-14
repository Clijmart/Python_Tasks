s = 'Guido van Rossum heeft programmeertaal Python bedacht.'
word = ''

for letter in s:
    if letter in ('aeiou'):
        word += letter

print(word)