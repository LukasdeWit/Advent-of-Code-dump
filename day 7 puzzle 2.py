bags = {}

def bag_count(bag):
    if not bags[bag]:
        return 1
    else:
        count = 1
        for b in bags[bag]:
            print(b)
            count += bag_count(b[0]) * b[1]
        print(count)
        return count

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

eq = "shiny gold"

amount = bag_count(eq) - 1

print(amount) # 8015
