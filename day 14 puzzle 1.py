yes_mask = 0
no_mask = 0

mem_dict = {}

def create_mask(line):
    cur_val = 1
    yes = 0
    no = 0
    for char in line[::-1]:
        if char == '1':
            yes += cur_val
            no += cur_val
        if char == 'X':
            no += cur_val
        cur_val *= 2
    return yes, no


for line in open("day 14 puzzle 1 data.txt"):
    op, val = line.split(" = ")
    if op[1] == 'a':
        yes_mask, no_mask = create_mask(val.strip('\n'))
    if op[1] == 'e':
        mem_dict[op] = (int(val) | yes_mask) & no_mask

count = sum(mem_dict.values())
print(count)
