search = 2020

f = open('day1.txt', 'r')
data = f.readlines()
data.pop(-1)
data = list(map(int, data))

while data != []:
    first = data.pop()

    for one in range(len(data)):
        for two in range(len(data)):
            if one != two:
                if first + data[one] + data[two] == search:
                    print(str(first * data[one] * data[two]))
                    exit(0)
