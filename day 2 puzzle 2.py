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
    firstpos = int(line[0].split('-')[0])
    secondpos = int(line[0].split('-')[1])
    char = line[1][0]
    password = line[2]
    if (password[firstpos - 1] == char) != (password[secondpos - 1] == char):
        correctcount += 1

print(correctcount) # ans = 727
