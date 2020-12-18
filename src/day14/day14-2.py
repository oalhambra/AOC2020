def generate_destinations(mask):
    if 'X' not in mask:
        return [int('0b' + mask, 2)]
    else:
        results = []
        results.extend(generate_destinations(mask[:mask.index('X') + 1].replace('X', '0') + mask[mask.index('X') + 1:]))
        results.extend(generate_destinations(mask[:mask.index('X') + 1].replace('X', '1') + mask[mask.index('X') + 1:]))
        return results


def apply_mask(mask, val):
    val = format(val, '036b')
    result = ''
    for i in range(len(mask)):
        if mask[i] == '0':
            result += val[i]
        else:
            result += mask[i]
    results = generate_destinations(result)
    return results


f = open('day14.txt', 'r')
data = f.readlines()

mask = ''
mem = dict()

for line in data:
    if 'mask' in line:
        mask = line.split('=')[1].strip()
    else:
        aux = line.split('=')
        dest = int(aux[0].replace('mem[', '').replace(']', ''))
        pre = int(aux[1])

        destinations = apply_mask(mask, dest)

        for d in destinations:
            mem[d] = pre

print(sum(mem.values()))
