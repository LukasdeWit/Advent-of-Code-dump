highest = 0

for row in open("day 5 puzzle 1 data.txt"):
    seat_nr = 0
    seat_inc = 512
    for char in row:
        if char in "BR":
            seat_nr += seat_inc
        seat_inc /= 2
    highest = max(highest, seat_nr)
    
print(highest) # 828
