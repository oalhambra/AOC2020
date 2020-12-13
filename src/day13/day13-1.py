f = open('day13.txt', 'r')
data = f.readlines()

timestamp = int(data[0])
buses = list(data[1].strip().split(','))
while 'x' in buses:
    buses.remove('x')
buses = list(map(int, buses))
print(timestamp)
print(buses)

reminders = list(map(lambda x: timestamp % x, buses))
print(reminders)
next_pass = []
for i in range(len(buses)):
    next_pass.append(buses[i] - reminders[i])
print(next_pass)
print(buses[next_pass.index(min(next_pass))] * min(next_pass))
