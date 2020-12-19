f = open('day15.txt', 'r')
data = f.read()
data = data.split(',')
data = list(map(int, data))

history = []
turn = 0
for i in data:
    history.insert(0, i)
    turn += 1

while turn < 2020:
    if history.count(history[0]) == 1:
        history.insert(0, 0)
    else:
        previous = history.index(history[0], 1)
        history.insert(0, previous)
    turn += 1
print(history[0])
