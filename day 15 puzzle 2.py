data = {}

pos = -1
prev = 0

for line in open("day 15 puzzle 1 data.txt"):
    for num in line.split(','):
        pos += 1
        data[int(num)] = pos
        prev = int(num)

del data[prev]

while pos < 30000000 - 1:
    if not prev in data:
        data[prev] = pos
        prev = 0
    else:
        old_pos = data[prev]
        data[prev] = pos
        prev = pos - old_pos
    pos += 1

print(prev)
