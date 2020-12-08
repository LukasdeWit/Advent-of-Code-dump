

def read_instructions():
    instructions = []
    for line in open("day 8 puzzle 1 data.txt"):
        inst, val = line.split()
        val = eval("0 " + val.strip("\n"))
        # [instruction, value, visited]
        instructions.append([inst, val, False])
    return instructions



def process(inst, val, op, acc):
    if inst == "acc":
        return op + 1, acc + val
    if inst == "jmp":
        return op + val, acc
    if inst == "nop":
        return op + 1, acc

size = len(read_instructions())

for current in range(size):
    instructions = read_instructions()
    if instructions[current][0] == "nop":
        instructions[current][0] = "jmp"
    elif instructions[current][0] == "jmp":
        instructions[current][0] = "nop"
    
    accumulator = 0
    operation = 0
    while operation < size and not instructions[operation][2] :
        instructions[operation][2] = True
        operation, accumulator = process(instructions[operation][0], instructions[operation][1], operation, accumulator)
    if operation >= size:
        print(accumulator) # 2096
