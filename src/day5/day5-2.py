f = open('day5.txt', 'r')
data = f.readlines()

max_seatId = 0

seatIds = []

for line in data:
    line = line.rstrip()
    row = line[:7]
    column = line[7:]

    row = row.replace('F', '0').replace('B', '1')
    column = column.replace('L', '0').replace('R', '1')
    row = int(row, base=2)
    column = int(column, base=2)
    seatId = row * 8 + column
    seatIds.append(seatId)

seatIds.sort()
allSeats = [i for i in range(seatIds[0], seatIds[-1])]
print(set(allSeats).difference(set(seatIds)).pop())
