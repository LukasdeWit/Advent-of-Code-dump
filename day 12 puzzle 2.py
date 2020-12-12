dir_names = ['N', 'E', 'S', 'W']
dir_vecs = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
x_pos_waypoint = 10
y_pos_waypoint = 1
x_pos = 0
y_pos = 0

def rotate(x, y, tics):
    if tics == 0:
        return x, y
    return rotate(-y, x, tics - 1)
    

for line in open("day 12 puzzle 1 data.txt"):
    op, val = line[0], int(line[1:])
    if op in "NESW":
        x_pos_waypoint += dir_vecs[op][0] * val
        y_pos_waypoint += dir_vecs[op][1] * val
    if op == 'F':
        x_pos += x_pos_waypoint * val
        y_pos += y_pos_waypoint * val
    if op == 'L':
        x_pos_waypoint, y_pos_waypoint = rotate(x_pos_waypoint, y_pos_waypoint, val // 90)
    if op == 'R':
        x_pos_waypoint, y_pos_waypoint = rotate(x_pos_waypoint, y_pos_waypoint, 4 - (val // 90))

print(abs(x_pos) + abs(y_pos))
