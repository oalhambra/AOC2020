f = open('day6.txt', 'r')
data = f.read()

groups = data.split('\n\n')

answer = 0

for group in groups:
    group = group.replace('\n', '')
    answer += len(set(group))
print(answer)
