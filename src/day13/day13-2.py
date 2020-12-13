def next_pass(timestamp, bus_id):
    return (bus_id - (timestamp % bus_id)) % bus_id


f = open('day13.txt', 'r')
data = f.readlines()
buses = list(data[1].strip().split(','))
parsed_buses = []  # contains bus + position in array AKA time after first bus that it needs to pass
clean_buses = []
expected_remaining = []
for i in range(len(buses)):
    try:
        clean_buses.append(int(buses[i]))
        expected_remaining.append(i % int(buses[i]))
    except ValueError:
        pass

a = 0
timestamp_expr = 'a'
matches = 0
iterations = 0
t_remaining = []

while t_remaining != expected_remaining:
    t_remaining = list(map(lambda x: next_pass(eval(timestamp_expr), x), clean_buses))

    if t_remaining[:matches + 1] == expected_remaining[:matches + 1]:
        timestamp_expr = timestamp_expr.replace('a', '(' + str(clean_buses[matches]) + '*a+' + str(iterations) + ')')
        matches += 1
        iterations = 0
        a = 0
    else:
        iterations += 1
        a += 1
print(eval(timestamp_expr))
