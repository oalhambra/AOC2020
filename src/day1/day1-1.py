search = 2020

f = open('day1.txt', 'r')
data = f.readlines()
data.pop(-1)
data = list(map(int, data))

while data != []:
    first = data.pop()
    for el in data:
        if first + el == search:
            print(str(first * el))
            exit(0)
