file = open("day 3 puzzle 1 data.txt")

reading = True
data = []
while reading:
    line = file.readline()
    if line == "":
        reading = False
    else:
        datapoint = list(line.split('\n')[0])
        data.append(datapoint)

x_max = len(data[0])
y_max = len(data)

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


mult = 1
for tup in steps:
    x_step, y_step = tup
    trees = 0
    x_curr = 0
    y_curr = 0
    while y_curr < y_max - 1:
        y_curr += y_step
        x_curr += x_step
        if x_curr >= x_max:
            x_curr -= x_max
        if data[y_curr][x_curr] == "#":
            trees += 1
    mult *= trees
    print(trees)

print(mult) # 736527114
