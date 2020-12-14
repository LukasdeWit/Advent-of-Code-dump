buses = []
early_time = 0

file = open("day 13 puzzle 1 data.txt")
early_time = int(file.readline())
for bus in file.readline().split(','):
    if not bus == 'x':
        buses.append(int(bus))

waittimes = []

for bus in buses:
    waittimes.append(bus - (early_time % bus))

index = waittimes.index(min(waittimes))
magic_number = waittimes[index] * buses[index]

print(magic_number)
