f = open('day4.txt', 'r')
data = f.read()

passports = data.split("\n\n")
passports = list(map(lambda x: x.replace("\n", " "), passports))

passport_dict = []
for passport in passports:
    aux = {}
    passport = passport.rstrip()
    passport = passport.split(" ")
    for entry in passport:
        val = entry.split(':')
        aux[val[0]] = val[1]
    passport_dict.append(aux)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
hacked_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = 0
for passport in passport_dict:
    if set(hacked_fields) & set(passport.keys()) == set(hacked_fields):
        valid_passports += 1
print(valid_passports)
