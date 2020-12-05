seats = [False] * 1024


for row in open("day 5 puzzle 1 data.txt"):
    seat_nr = 0
    seat_inc = 512
    for char in row:
        if char in "BR":
            seat_nr += seat_inc
        seat_inc //= 2
    seats[seat_nr] = True

curr_seat = seats.index(True)

while seats[curr_seat]:
    curr_seat += 1

print(curr_seat) # 565
