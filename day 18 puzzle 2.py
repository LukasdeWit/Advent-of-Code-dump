

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
        

def tokenize(problem):
    if '*' in problem:
        index = problem.index('*')
        return ['*', tokenize(problem[:index]), tokenize(problem[index + 1:])]
    if '+' in problem:
        index = problem.index('+')
        return ['+', tokenize(problem[:index]), tokenize(problem[index + 1:])]
    if type(problem[0]) is int:
        return problem[0]
    if type(problem[0]) is list:
        return tokenize(problem[0])


def solve(problem):
    if type(problem) is int:
        return problem
    if problem[0] == '+':
        return solve(problem[1]) + solve(problem[2])
    if problem[0] == '*':
        return solve(problem[1]) * solve(problem[2])


total = 0

for line in open("day 18 puzzle 1 data.txt"):
    problem = parse(line.strip('\n').replace(' ', ''))
    tokens = tokenize(problem)
    solution = solve(tokens)
    total += solution

print(total)
