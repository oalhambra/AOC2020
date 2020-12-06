f = open('day6.txt', 'r')
data = f.read()

groups = data.split('\n\n')

answer = 0

for group in groups:
    people = group.split('\n')
    group_set = set(people[0])
    for person in people:
        group_set = group_set & set(person)
    answer += len(group_set)
print(answer)
