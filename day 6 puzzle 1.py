total = 0

first_line = True
all_chars = ""

for l in open("day 6 puzzle 1 data.txt"):
    line = l.replace('\n', '')
    if line == "":
        total += len(all_chars)
        all_chars = ""
        first_line = True
    else:
        if first_line:
            first_line = False
            all_chars = line
        else:
            for char in all_chars:
                if not char in line:
                    all_chars = all_chars.replace(char, '')
                    

total += len(all_chars)
            
print(total) # 3394
