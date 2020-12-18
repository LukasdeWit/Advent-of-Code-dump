
def find_closing_parenthesis_index(line, index):
    depth = 0
    for i in range(index, len(line)):
        if line[i] == '(':
            depth += 1
        if line[i] == ')':
            depth -= 1
            if depth == 0:
                return i
    raise ValueError


def parse(line):
    index = 0
    problem = []
    while index < len(line):
        if line[index] == '(':
            close = find_closing_parenthesis_index(line, index)
            problem.append(parse(line[index + 1 : close]))
            index = close
        elif line[index] in "+*":
            problem.append(line[index])
        else:
            problem.append(int(line[index]))
        index += 1
    return problem

def solve(problem):
    n = 0
    index = 1
    if type(problem[0]) is list:
        n = solve(problem[0])
    else:
        n = problem[0]
    while index < len(problem):
        if problem[index] == '+':
            if type(problem[index + 1]) is list:
                n += solve(problem[index + 1])
            else:
                n += problem[index + 1]
        else:
            if type(problem[index + 1]) is list:
                n *= solve(problem[index + 1])
            else:
                n *= problem[index + 1]
        index += 2
    return n
        
        
total = 0

for line in open("day 18 puzzle 1 data.txt"):
    problem = parse(line.strip('\n').replace(' ', ''))
    solution = solve(problem)
    total += solution

print(total)
    
