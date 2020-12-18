max_cycles = 6
cycle = 0

y_in = 0
universe = []

# open("day 17 puzzle 1 data small.txt")

for line in open("day 17 puzzle 1 data.txt"):
    for i in range(len(line.strip('\n'))):
        if line[i] == '#':
            universe.append([i, y_in, 0, 0])
    y_in += 1

dyn_get_neighbours = {}
def get_all_neighbours(pos):
    if str(pos) in dyn_get_neighbours:
        return dyn_get_neighbours[str(pos)]
    x, y, z, w= pos
    neighbours = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    neighbours.append([x + i, y + j, z + k, w + l])
    neighbours.remove(pos)
    dyn_get_neighbours[str(pos)] = neighbours
    return neighbours
    


def next_universe(prev):
    next_uni = []
    all_neighbours = {}
    for pos in prev:
        for neighbour in get_all_neighbours(pos):
            if str(neighbour) in all_neighbours:
                all_neighbours[str(neighbour)] += 1
            else:
                all_neighbours[str(neighbour)] = 1
    for neighbour in all_neighbours:
        pos = [int(i) for i in neighbour.strip('[]').split(", ")]
        if (pos in prev and all_neighbours[neighbour] in [2, 3]) or (not pos in prev and all_neighbours[neighbour] == 3):
            next_uni.append(pos)
    return next_uni


while cycle < max_cycles:
    print(cycle, len(universe))
    universe = next_universe(universe)
    cycle += 1
    
print(cycle)

print(len(universe))
