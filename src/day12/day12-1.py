def move_dir(direction, distance):
    return direction[0] * distance, direction[1] * distance


f = open('day12.txt', 'r')
data = f.readlines()

north = (1, 0)
south = (-1, 0)
east = (0, 1)
west = (0, -1)
dirs = [north, east, south, west]

direction = east
pos = (0, 0)

for line in data:
    if line[:1] == 'N':
        translation = move_dir(north, int(line[1:]))
        pos = (pos[0] + translation[0], pos[1] + translation[1])
    elif line[:1] == 'S':
        translation = move_dir(south, int(line[1:]))
        pos = (pos[0] + translation[0], pos[1] + translation[1])
    elif line[:1] == 'E':
        translation = move_dir(east, int(line[1:]))
        pos = (pos[0] + translation[0], pos[1] + translation[1])
    elif line[:1] == 'W':
        translation = move_dir(west, int(line[1:]))
        pos = (pos[0] + translation[0], pos[1] + translation[1])
    elif line[:1] == 'R':
        index = dirs.index(direction)
        increment = int(line[1:]) / 90
        direction = dirs[int((index + increment) % 4)]
        pass
    elif line[:1] == 'L':
        index = dirs.index(direction)
        increment = int(line[1:]) / 90
        direction = dirs[int((index - increment) % 4)]
        pass
    elif line[:1] == 'F':
        translation = move_dir(direction, int(line[1:]))
        pos = (pos[0] + translation[0], pos[1] + translation[1])

print(abs(pos[0]) + abs(pos[1]))
