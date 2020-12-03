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

x_curr = 0
y_curr = 0

x_step = 3
y_step = 1

trees = 0

while y_curr < y_max - 1:
    y_curr += y_step
    x_curr += x_step
    if x_curr >= x_max:
        x_curr -= x_max
    if data[y_curr][x_curr] == "#":
        trees += 1

print(trees) # 167
