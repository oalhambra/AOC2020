def expansion(base_list, inv_storage):
    new_list = set(base_list)
    for el in base_list:
        try:
            bags = inv_storage[el]
            for item in bags:
                new_list.add(item[0])
        except KeyError:
            pass
    return new_list, len(base_list) == len(new_list)


f = open('day7.txt', 'r')
data = f.readlines()

storage = {}
for line in data:
    aux = line.split('contain')
    container = aux[0].replace('bags', '').rstrip()
    contained = aux[1].replace('.', '').replace('bags', '').replace('bag', '').split(',')
    contained = list(map(lambda x: x.strip(), contained))
    storage[container] = contained

inv_storage = dict()
for key, value in storage.items():
    for el in value:
        if el[:2] == 'no':
            inv_storage.setdefault(el[2:], list()).append([key, 0])
        else:
            inv_storage.setdefault(el[2:], list()).append([key, int(el[:2])])

base = {'shiny gold'}
same_size = False

while not same_size:
    base, same_size = expansion(base, inv_storage)
base.discard('shiny gold')
print(len(base))
