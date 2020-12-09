data = []
preamble_size = 25

for line in open("day 9 puzzle 1 data.txt"):
    data.append(int(line.strip('\n')))

def check(listy, nums, index):
    val = listy[index]
    for i in range(nums - 1):
        for j in range(i + 1, nums):
            if listy[index - nums + i] + listy[index - nums + j] == val:
                print(str(listy[index - nums + i]) + " + " + str(listy[index - nums + j]) + " = " + str(val))
                return True
    print("!!!!!!!!!!!!! " + str(index) + ": " + str(val) + " !!!!!!!!!!!!!!")
    return False


for i in range(preamble_size, len(data)):
    if not check(data, preamble_size, i):
        print(data[i]) # 14144619
        break
