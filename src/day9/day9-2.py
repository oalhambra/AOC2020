f = open('day9.txt', 'r')
data = f.readlines()

data = list(map(int, data))
preamble = 25
weakpoint = 0
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
        weakpoint = data[i]
        print(weakpoint)
        break
probable = []
for el in data:
    probable.append(el)
    acc = sum(probable)
    while acc > weakpoint:
        probable.pop(0)
        acc = sum(probable)
    if acc == weakpoint:
        print('success')
        weakness = min(probable) + max(probable)
        print(weakness)
        break
