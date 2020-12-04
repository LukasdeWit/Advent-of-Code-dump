import copy

correct_passwords = 0

correct_pp = {"byr":"", "iyr":"", "eyr":"", "hgt":"", "hcl":"", "ecl":"", "pid":"", "cid":""}
passport = {}

def check(pp):
    return "byr" in pp and "iyr" in pp and "eyr" in pp and "hgt" in pp and "hcl" in pp and "ecl" in pp and "pid" in pp

for string in open("day 4 puzzle 1 data.txt"):
    line = string.replace('\n', '')
    if line == '':
        if check(passport):
            correct_passwords += 1
        passport = {}
    else:
        for pair in line.split(" "):
            passport[pair.split(':')[0]] = pair.split(':')[1]




print(correct_passwords)
