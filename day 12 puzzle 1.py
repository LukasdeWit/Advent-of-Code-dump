dir_names = ['N', 'E', 'S', 'W']
dir_vecs = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
current_dir = 'E'
x_pos = 0
y_pos = 0

for line in open("day 12 puzzle 1 data.txt"):
    op, val = line[0], int(line[1:])
    if op in "NESW":
        x_pos += dir_vecs[op][0] * val
        y_pos += dir_vecs[op][1] * val
    if op == 'F':
        x_pos += dir_vecs[current_dir][0] * val
        y_pos += dir_vecs[current_dir][1] * val
    if op == 'L':
        current_dir = dir_names[dir_names.index(current_dir) - val // 90]
    if op == 'R':
        current_dir = dir_names[(dir_names.index(current_dir) + val // 90) % 4]

print(abs(x_pos) + abs(y_pos))
