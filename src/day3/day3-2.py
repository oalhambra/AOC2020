f = open('day3.txt', 'r')
data = f.readlines()

oneCount = 0
threeCount = 0
fiveCount = 0
sevenCount = 0
evenCount = 0

pos1 = 0
pos3 = 0
pos5 = 0
pos7 = 0
posEven = 0
even = True
for line in data:
    line = line.replace("\n", '')
    if line[pos1 % len(line)] == '#':
        oneCount += 1
    if line[pos3 % len(line)] == '#':
        threeCount += 1
    if line[pos5 % len(line)] == '#':
        fiveCount += 1
    if line[pos7 % len(line)] == '#':
        sevenCount += 1
    if line[posEven % len(line)] == '#' and even:
        evenCount += 1
    pos1 += 1
    pos3 += 3
    pos5 += 5
    pos7 += 7

    if not even:
        posEven += 1
    even = not even

print(str(evenCount * oneCount * threeCount * fiveCount * sevenCount))
