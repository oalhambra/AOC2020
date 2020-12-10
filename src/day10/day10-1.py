f = open('day10.txt', 'r')
data = f.readlines()
data = list(map(int, data))

data.sort()
data.append(data[-1] + 3)
diffs = [data[0]]
for i in range(1, len(data)):
    diffs.append(data[i] - data[i - 1])
print(diffs.count(1) * diffs.count(3))
