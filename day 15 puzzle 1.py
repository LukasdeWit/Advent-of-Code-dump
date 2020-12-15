data = []

for line in open("day 15 puzzle 1 data.txt"):
    for num in line.split(','):
        data.insert(0, int(num))

while len(data) < 2020:
    if data[0] in data[1:]:
        data.insert(0, data.index(data[0], 1))
    else:
        data.insert(0, 0)

print(data[0])
