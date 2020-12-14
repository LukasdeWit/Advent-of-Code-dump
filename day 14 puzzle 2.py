x_clear_mask = ""
x_add_mask = ""
yes_mask = 0

mem_dict = {}

def create_mask(line):
    bit = 1
    yes = 0
    for char in line[::-1]:
        if char == '1':
            yes += bit
        bit += bit
    return yes, line.replace('0', '1').replace('X', '0'), line.replace('1', '0')

def get_mask_num(mask):
    total = 0
    bit = 1
    for char in mask[::-1]:
        if char == '1':
            total += bit
        bit += bit
    return total

def get_addresses(address, mask, clear_mask):
    add_list = []
    if 'X' in mask: # the worst pattern matching i ever did and i did cpl twice
        add_list += get_addresses(address, mask.replace('X', '0', 1), clear_mask)
        add_list += get_addresses(address, mask.replace('X', '1', 1), clear_mask)
        return add_list
    else:
        return [(address & get_mask_num(clear_mask)) | get_mask_num(mask)]
    

for line in open("day 14 puzzle 1 data.txt"):
    op, val = line.split(" = ")
    if op[1] == 'a':
        yes_mask, x_clear_mask, x_add_mask = create_mask(val.strip('\n'))
    if op[1] == 'e':
        for address in get_addresses(yes_mask | int(op.strip("me[]")), x_add_mask, x_clear_mask):
            mem_dict[str(address)] = int(val)

count = sum(mem_dict.values())
print(count)
