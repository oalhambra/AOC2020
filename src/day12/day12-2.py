def move_dir(direction, distance):
    return direction[0] * distance, direction[1] * distance


def rotate_waypoint(waypoint, angle, direction):
    new_waypoint = waypoint
    if angle == 90:
        if direction == 'R':
            new_waypoint = (-waypoint[1], waypoint[0])
        else:
            new_waypoint = rotate_waypoint(waypoint, 270, 'R')
    elif angle == 180:
        new_waypoint = (-waypoint[0], -waypoint[1])
    elif angle == 270:
        if direction == 'R':
            new_waypoint = (waypoint[1], -waypoint[0])
        else:
            new_waypoint = rotate_waypoint(waypoint, 90, 'R')
    return new_waypoint


f = open('day12.txt', 'r')
data = f.readlines()

north = (1, 0)
south = (-1, 0)
east = (0, 1)
west = (0, -1)

pos = (0, 0)
waypoit_pos = (1, 10)

for line in data:
    if line[:1] == 'N':
        translation = move_dir(north, int(line[1:]))
        waypoit_pos = (waypoit_pos[0] + translation[0], waypoit_pos[1] + translation[1])
    elif line[:1] == 'S':
        translation = move_dir(south, int(line[1:]))
        waypoit_pos = (waypoit_pos[0] + translation[0], waypoit_pos[1] + translation[1])
    elif line[:1] == 'E':
        translation = move_dir(east, int(line[1:]))
        waypoit_pos = (waypoit_pos[0] + translation[0], waypoit_pos[1] + translation[1])
    elif line[:1] == 'W':
        translation = move_dir(west, int(line[1:]))
        waypoit_pos = (waypoit_pos[0] + translation[0], waypoit_pos[1] + translation[1])
    elif line[:1] == 'R':
        waypoit_pos = rotate_waypoint(waypoit_pos, int(line[1:]), 'R')
        pass
    elif line[:1] == 'L':
        waypoit_pos = rotate_waypoint(waypoit_pos, int(line[1:]), 'L')
        pass
    elif line[:1] == 'F':
        translation = move_dir(waypoit_pos, int(line[1:]))
        pos = (pos[0] + translation[0], pos[1] + translation[1])

print(abs(pos[0]) + abs(pos[1]))
