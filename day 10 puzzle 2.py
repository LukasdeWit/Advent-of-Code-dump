data = []

for line in open("day 10 puzzle 1 data.txt"):
    data.append(int(line.strip('\n')))

data.append(0)
data.sort()

dyn = dict.fromkeys(range(data[-1] + 3))
dyn[data[-1]] = 1
    

def rec_adapt(listy, val):
    if not val in listy:
        return 0
    if not dyn[val]:
        dyn[val] = rec_adapt(listy, val + 1) + rec_adapt(listy, val + 2) + rec_adapt(listy, val + 3)
    return dyn[val]
        
    

print(rec_adapt(data, data[0])) # 1973822685184

