f = open('day2.txt', 'r')
data = f.readlines()

counter = 0
for i in data:
    i = i.replace(':', '')
    aux = i.split(' ')
    margin = aux[0].split('-')

    if aux[2].count(aux[1]) in range(int(margin[0]), int(margin[1]) + 1):
        counter += 1
print(counter)
