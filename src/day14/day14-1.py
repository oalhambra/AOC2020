def apply_mask(mask, val):
    val = format(val, '036b')
    result = '0b'
    for i in range(len(mask)):
        if mask[i] != 'X':
            result += mask[i]
        else:
            result += val[i]
    return int(result, 2)


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
        mem[dest] = apply_mask(mask, pre)

print(sum(mem.values()))
