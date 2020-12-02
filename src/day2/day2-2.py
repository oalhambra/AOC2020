f = open('day2.txt', 'r')
data = f.readlines()

counter = 0
for i in data:
    i = i.replace(':', '')
    aux = i.split(' ')
    margin = aux[0].split('-')

    if (aux[2][int(margin[0]) - 1] == aux[1]) ^ (aux[2][int(margin[1]) - 1] == aux[1]):
        counter += 1
print(counter)
