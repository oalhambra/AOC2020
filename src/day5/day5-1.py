f = open('day5.txt', 'r')
data = f.readlines()

max_seatId = 0

for line in data:
    line = line.rstrip()
    row = line[:7]
    column = line[7:]

    row = row.replace('F', '0').replace('B', '1')
    column = column.replace('L', '0').replace('R', '1')
    row = int(row, base=2)
    column = int(column, base=2)
    seatId = row * 8 + column
    max_seatId = max(max_seatId, seatId)

print(max_seatId)
