from copy import deepcopy

f = open('day11.txt', 'r')
data = f.readlines()
adyacent_tuples = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]

data = list(map(lambda x: x.strip(), data))
boat_seats = list(map(list, data))
nex_iteration = deepcopy(boat_seats)
stable = False

while not stable:
    boat_seats = deepcopy(nex_iteration)
    for i in range(len(boat_seats)):
        for j in range(len(boat_seats[i])):
            if boat_seats[i][j] == '.':
                continue
            adyacent_counter = 0
            for seat in adyacent_tuples:
                try:
                    if boat_seats[seat[0] + i][seat[1] + j] == '#':
                        if seat[0] + i >= 0 and seat[1] + j >= 0:
                            adyacent_counter += 1
                except IndexError:
                    pass

            if boat_seats[i][j] == 'L' and adyacent_counter == 0:
                nex_iteration[i][j] = '#'

            elif boat_seats[i][j] == '#' and adyacent_counter >= 4:
                nex_iteration[i][j] = 'L'
    if boat_seats == nex_iteration:
        stable = True
print(sum(map(lambda x: x.count('#'), boat_seats)))
