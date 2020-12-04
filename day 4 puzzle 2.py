import copy

correct_passwords = 0

correct_pp = {"byr":"", "iyr":"", "eyr":"", "hgt":"", "hcl":"", "ecl":"", "pid":"", "cid":""}
hexa = "0123456789abcdef"
dec = "0123456789"
eyecolours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
passport = {}

def check_hgt(pp):
    if "hgt" in pp:
        hgt = pp["hgt"]
        if "in" in hgt:
            num = int(hgt.replace("in", ""))
            return num >= 59 and num <= 76
        elif "cm" in hgt:
            num = int(hgt.replace("cm", ""))
            return num >= 150 and num <= 193
    return False

def check_hcl(pp):
    if "hcl" in pp:
        hcl = pp["hcl"]
        if len(hcl) == 7 and hcl[0] == '#':
            for char in hcl[1:]:
                if not char in hexa:
                    return False
            return True
    return False

def check_ecl(pp):
    if "ecl" in pp:
        return pp["ecl"] in eyecolours
    return False

def check_pid(pp):
    if "pid" in pp:
        pid = pp["pid"]
        if len(pid) == 9:
            for char in pid:
                if not char in dec:
                    return False
            return True
    return False

def check(pp):
    valid = True
    valid = valid and "byr" in pp and int(pp["byr"]) >= 1920 and int(pp["byr"]) <= 2002
    valid = valid and "iyr" in pp and int(pp["iyr"]) >= 2010 and int(pp["iyr"]) <= 2020
    valid = valid and "eyr" in pp and int(pp["eyr"]) >= 2020 and int(pp["eyr"]) <= 2030
    valid = valid and check_hgt(pp)
    valid = valid and check_hcl(pp)
    valid = valid and check_ecl(pp)
    return valid and check_pid(pp)

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
