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
valid_tickets = []
for t in all_tickets:
    valid = True
    for entry in t:
        if not follows_any_rule(all_rules, entry):
            not_valid += entry
            valid = False
    if valid:
        valid_tickets.append(t)

rule_possible_position = dict()

for rule in rules_dict.keys():
    rule_possible_position[rule] = []
    for i in range(len(rules_dict.keys())):
        valid_rule = True
        for t in valid_tickets:
            # print(t, rule)
            if not follows_any_rule(rules_dict[rule], t[i]):
                valid_rule = False
        if valid_rule:
            rule_possible_position[rule].append(i)

ticket_values = dict()

while len(ticket_values.keys()) < len(my_ticket):
    for key, value in rule_possible_position.items():
        if len(value) == 1:
            position = value[0]
            ticket_values[key] = my_ticket[position]
            for k, v in rule_possible_position.items():
                if position in v:
                    rule_possible_position[k].remove(position)
            break

result = 1
for k in ticket_values.keys():
    if 'departure' in k:
        result *= ticket_values[k]
print(result)
