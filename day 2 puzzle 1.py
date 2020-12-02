file = open("day 2 puzzle 1 data.txt")

reading = True
data = []
while reading:
    line = file.readline()
    if line == "":
        reading = False
    else:
        listlines = line.split()
        data.append(listlines)

correctcount = 0

for line in data:
    minval = int(line[0].split('-')[0])
    maxval = int(line[0].split('-')[1])
    char = line[1][0]
    password = line[2]
    charamount = 0
    for c in password:
        if c == char:
            charamount += 1
    if charamount >= minval and charamount <= maxval:
        correctcount += 1

print(correctcount) # ans = 620
