def follows_any_rule(rules, val):
    valid = False
    for rule in rules:
        if val >= rule[0] and val <= rule[1]:
            valid = True
    return valid


f = open('day16.txt', 'r')
data = f.read()
data = data.split("\n\n")

rules_dict = dict()
rules = data[0]
rules = rules.split("\n")
for rule in rules:
    aux = rule.split(':')
    ranges = aux[1].split("or")
    ran = list(map(lambda x: list(map(int, x.split('-'))), ranges))
    rules_dict[aux[0]] = ran

aux = list(rules_dict.values())
all_rules = []
for r in rules_dict.values():
    all_rules.extend(r)

my_ticket = data[1]
my_ticket = my_ticket.split('\n')[1].split(',')
my_ticket = list(map(int, my_ticket))

all_tickets = data[2]
all_tickets = all_tickets.strip().split('\n')[1:]
all_tickets = list(map(lambda x: x.split(','), all_tickets))
all_tickets = list(map(lambda x: list(map(int, x)), all_tickets))

not_valid = 0
for t in all_tickets:
    for entry in t:
        if not follows_any_rule(all_rules, entry):
            not_valid += entry
print(not_valid)
