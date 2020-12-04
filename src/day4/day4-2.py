import re

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

valid_byr = "^19[2-9][0-9]$|^200[0-2]$"
valid_iyr = "^201[0-9]$|^2020$"
valid_eyr = "^202[0-9]$|^2030$"
valid_hgt = "^1([5-8][0-9]|9[0-3])cm$|^(59|6[0-9]|7[0-6])in$"
valid_hcl = "^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$"
valid_ecl = "^(amb|blu|brn|gry|grn|hzl|oth)$"
valid_pid = "^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"

for passport in passport_dict:
    valid = True
    if set(hacked_fields) & set(passport.keys()) != set(hacked_fields):
        valid = False
    else:
        if not re.search(valid_byr, passport['byr']):
            valid = False
        if not re.search(valid_iyr, passport['iyr']):
            valid = False
        if not re.search(valid_eyr, passport['eyr']):
            valid = False
        if not re.search(valid_hgt, passport['hgt']):
            valid = False
        if not re.search(valid_hcl, passport['hcl']):
            valid = False
        if not re.search(valid_ecl, passport['ecl']):
            valid = False
        if not re.search(valid_pid, passport['pid']):
            valid = False
    if valid:
        valid_passports += 1

print(valid_passports)
