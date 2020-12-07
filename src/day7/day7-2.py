def inside(color):
    bags = storage[color]
    counter = 0

    for bag in bags:

        if bag[:2] == 'no':
            counter += 0
        else:
            el = bag.split(' ', 1)
            counter += int(el[0]) + (int(el[0]) * inside(el[1]))
    return counter


f = open('day7.txt', 'r')
data = f.readlines()

storage = {}
for line in data:
    aux = line.split('contain')
    container = aux[0].replace('bags', '').rstrip()
    contained = aux[1].replace('.', '').replace('bags', '').replace('bag', '').split(',')
    contained = list(map(lambda x: x.strip(), contained))
    storage[container] = contained

print(inside('shiny gold'))
