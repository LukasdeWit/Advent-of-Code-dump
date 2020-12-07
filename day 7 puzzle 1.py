bags = {}

def bag_rec(key, string):
    if not bags[key]:
        return False
    else:
        for bag in bags[key]:
            if bag[0] == string:
                return True
            else:
                if bag_rec(bag[0], string):
                    return True

for line in open("day 7 puzzle 1 data.txt"):
    line = line.replace('\n', '')
    bagtype, rest = line.split(" bags contain ")
    bags[bagtype] = []
    if not rest == "no other bags.":
        contents = rest.split(", ")
        for c in contents:
            c = c.replace(" bags", "").replace(" bag", "").replace(".", "")
            c_bag = c[2:]
            c_amount = int(c[0])
            bags[bagtype].append([c_bag, c_amount])

amount = 0
eq = "shiny gold"

for b in bags:
    if bag_rec(b, eq):
        amount += 1

print(amount) # 372
