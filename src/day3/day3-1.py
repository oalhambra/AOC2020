f = open('day3.txt', 'r')
data = f.readlines()

treeCount = 0
posX = -3
for line in data:
    line = line.replace("\n", '')
    posX += 3
    if line[posX % len(line)] == '#':
        treeCount += 1

print(treeCount)
