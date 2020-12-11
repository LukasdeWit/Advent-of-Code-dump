data = []

for line in open("day 10 puzzle 1 data.txt"):
    data.append(int(line.strip('\n')))

data.append(0)
data.sort()
for p in data:
    print(p)
data.append(data[-1] + 3)

count_ones = 0
count_threes = 0

for num in data:
    if num + 1 in data:
        count_ones += 1
    elif num + 3 in data:
        count_threes += 1
    

print(count_ones * count_threes) # 2470

