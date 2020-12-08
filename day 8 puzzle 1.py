instructions = []

for line in open("day 8 puzzle 1 data.txt"):
    inst, val = line.split()
    val = eval("0 " + val.strip("\n"))
    # [instruction, value, visited]
    instructions.append([inst, val, False])



def process(inst, val, op, acc):
    if inst == "acc":
        return op + 1, acc + val
    if inst == "jmp":
        return op + val, acc
    if inst == "nop":
        return op + 1, acc


accumulator = 0
operation = 0

while not instructions[operation][2]:
    instructions[operation][2] = True
    operation, accumulator = process(instructions[operation][0], instructions[operation][1], operation, accumulator)

print(accumulator)
