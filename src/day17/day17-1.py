def adyacent_dimensions(dimension):
    if dimension == 1:
        result = []
        for i in range(-1, 2):
            result.append((i,))
        return result
    else:
        previous_dimension = adyacent_dimensions(dimension - 1)
        result = []
        for i in range(-1, 2):
            for p in previous_dimension:
                result.append((p + (i,)))
        return result


f = open('day17.txt', 'r')
data = f.readlines()
dimension = 3
zero = tuple()
for i in range(dimension):
    zero += (0,)
clear = tuple()
active = []
for i in range(dimension - 2):
    clear += (0,)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            active.append((i, j) + clear)

adyacents = adyacent_dimensions(dimension)
adyacents.remove(zero)

for _ in range(6):
    next_round = dict()
    for position in active:
        for a in adyacents:
            a_pos = tuple(map(lambda i, j: i + j, position, a))
            if a_pos in next_round.keys():
                next_round[a_pos] += 1
            else:
                next_round[a_pos] = 1
    next_active = []
    for k, v in next_round.items():
        if k in active:
            if v == 2 or v == 3:
                next_active.append(k)
        else:
            if v == 3:
                next_active.append(k)
    active = next_active
print(len(active))
