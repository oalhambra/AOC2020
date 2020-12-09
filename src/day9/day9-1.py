f = open('day9.txt', 'r')
data = f.readlines()

data = list(map(int, data))
preamble = 25

for i in range(preamble, len(data)):
    valid = False
    pre_list = data[i - preamble:i]
    for j in range(len(pre_list)):
        for k in range(j + 1, len(pre_list)):
            if data[i] == pre_list[j] + pre_list[k]:
                valid = True
                break
        if valid:
            break
    if not valid:
        print(data[i])
        break
