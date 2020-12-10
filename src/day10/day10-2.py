f = open('day10.txt', 'r')
data = f.readlines()
data = list(map(int, data))

data.sort()
data.append(data[-1] + 3)
diffs = [data[0]]
for i in range(1, len(data)):
    diffs.append(data[i] - data[i - 1])

group_sizes = []
size = 0
for i in diffs:
    if i == 3:
        group_sizes.append(size)
        size = 0
    if i == 1:
        size += 1

combos = 1
for g in group_sizes:
    if g == 2:
        combos *= 2
    if g == 3:
        combos *= 4
    if g == 4:
        combos *= 7
print(combos)
