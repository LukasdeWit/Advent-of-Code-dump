data = []
preamble_size = 25

for line in open("day 9 puzzle 1 data.txt"):
    data.append(int(line.strip('\n')))

def check_invalid(listy, nums, index):
    val = listy[index]
    for i in range(nums - 1):
        for j in range(i + 1, nums):
            if listy[index - nums + i] + listy[index - nums + j] == val:
                print(str(listy[index - nums + i]) + " + " + str(listy[index - nums + j]) + " = " + str(val))
                return True
    print("!!!!!!!!!!!!! " + str(index) + ": " + str(val) + " !!!!!!!!!!!!!!")
    return False

def check_sequence(listy, val, index):
    if val == 0:
        return True
    if val < 0:
        return False
    return check_sequence(listy, val - listy[index], index + 1)

def check_final_index(listy, val, index):
    if val == 0:
        return index - 1
    return check_final_index(listy, val - listy[index], index + 1)

def find_small_large(listy, start, end):
    small = 9999999999999999999999999999999999999
    large = 0
    for i in range(start, end + 1):
        if listy[i] < small:
            small = listy[i]
        if listy[i] > large:
            large = listy[i]
    return small, large

invalid = 0
weakness = 0

# find the invalid number
for i in range(preamble_size, len(data)):
    if not check_invalid(data, preamble_size, i):
        invalid = data[i]
        break

for i in range(preamble_size, len(data)):
    if check_sequence(data, invalid, i):
        final_index = check_final_index(data, invalid, i)
        small, large = find_small_large(data, i, final_index)
        weakness = small + large
        break

print(weakness)
