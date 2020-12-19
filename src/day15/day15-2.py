f = open('day15.txt', 'r')
data = f.read()
data = data.split(',')
data = list(map(int, data))
history_dict = dict()

turn = 0
for i in data:
    history_dict[i] = (turn, -1)
    turn += 1

val = (turn, -1)
new = True

while turn < 30000000:

    if new:
        val = (turn, history_dict[0][0])
        history_dict[0] = val
        new = False
    else:
        next_key = val[0] - val[1]
        if next_key in history_dict.keys():
            val = (turn, history_dict[next_key][0])
            new = False
        else:
            val = (turn, -1)
            new = True
        history_dict[next_key] = val
    turn += 1
for previous, pair in history_dict.items():
    if val == pair:
        break
print(previous)
