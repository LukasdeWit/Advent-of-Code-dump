ticket_data = {}
your_ticket = []
nearby_tickets = []

#the phases are: 0 = ticket attributes, 1 = your ticket, 2 = nearby tickets, 3 = done
phase = 0

def make_ticket(line):
    ticket = []
    for val in line.split(','):
        ticket.append(int(val))
    return ticket

for line in open("day 16 puzzle 1 data.txt"):
    if line == '\n':
        phase += 1
    else:
        data = line.strip('\n')
        if data == "your ticket:" or data == "nearby tickets:":
            pass
        else:
            if phase == 0:
                field, vals = data.split(": ")
                ticket_data[field] = []
                for val in vals.split(" or "):
                    lo, hi = val.split('-')
                    ticket_data[field] += range(int(lo), int(hi) + 1)
            elif phase == 1:
                your_ticket = make_ticket(data)
            elif phase == 2:
                nearby_tickets.append(make_ticket(data))

error_rate = 0
for ticket in nearby_tickets:
    for box in ticket:
        valid = False
        for value in ticket_data.values():
            if box in value:
                valid = True
                break
        if not valid:
            error_rate += box

print(error_rate)
