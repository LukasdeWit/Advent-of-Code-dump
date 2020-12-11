data = []

for line in open("day 11 puzzle 1 data.txt"):
    data.append(line.strip('\n'))


def chair_next_cycle(chairs, x_pos, y_pos):
    if chairs[y_pos][x_pos] == '.':
        return '.'
    count_full = 0
    count_empty = 0
    for x in [x_pos - 1, x_pos, x_pos + 1]:
        for y in [y_pos - 1, y_pos, y_pos + 1]:
            if not x < 0 and not x >= len(chairs[0]) and not y < 0 and not y >= len(chairs) and not (x == x_pos and y == y_pos):
                if chairs[y][x] == '#':
                    count_full += 1
                if chairs[y][x] == 'L':
                    count_empty += 1
    if chairs[y_pos][x_pos] == 'L' and count_full == 0:
        return '#'
    if chairs[y_pos][x_pos] == '#' and count_full >= 4:
        return 'L'
    return chairs[y_pos][x_pos]


def calc_chairs(chairs):
    next_chairs = []
    for i in range(len(chairs)):
        next_chairs.append("")
        for j in range(len(chairs[0])):
            next_chairs[i] += chair_next_cycle(chairs, j, i)
    return next_chairs


def check_chairs(old, new):
    for i in range(len(old)):
        if not old[i] == new[i]:
            return False
    return True


# draw for fun and profit
def draw_chairs(chairs):
    for line in chairs:
        print(line)
    print("\n=================================================================================\n")

previous = []
new = data
# aaargh why doesn't python have do-while loops
looping = True
while looping:
    previous = new
    new = calc_chairs(new)
    looping = not check_chairs(previous, new)
    #draw_chairs(new)    # uncomment this line to draw, for fun and profit

count = 0
for line in new:
    for c in line:
        if c == '#':
            count += 1

print(count)
