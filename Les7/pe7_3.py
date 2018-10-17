kaartnummers = open('kaartnummers.txt')
lines = kaartnummers.readlines()
numbers = []

for line in lines:
    numbers.append(int(line[:line.index(',')]))

maxNumber = max(numbers)

print('Deze file telt ' + str(len(numbers)) + ' regels.')
print('Het grootste kaartnummer is: ' + str(maxNumber) + ' en dat staat op regel ' + str(numbers.index(maxNumber) + 1) + '.')
