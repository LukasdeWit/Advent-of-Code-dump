file = open("day 1 puzzle 1 data.txt")

reading = True
data = []
while reading:
    line = file.readline()
    if line == "":
        reading = False
    else:
        datapoint = int(line)
        data.append(datapoint)

index = 0
mult = 0
while index < len(data):
    a = data[index]
    num = 2020 - a
    for b in data[index+1:len(data)-2]:
        num2 = num - b
        for c in data[data.index(b)+1:len(data)-1]:
            if c == num2:
                mult = a*b*c
                index = len(data)
    index += 1

print(mult)
