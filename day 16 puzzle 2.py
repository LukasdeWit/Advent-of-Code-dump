ticket_data = {}
your_ticket = []
nearby_tickets = []
valid_ticket = []

#the phases are: 0 = ticket attributes, 1 = your ticket, 2 = nearby tickets, 3 = done
phase = 0

def make_ticket(line):
    ticket = []
    for val in line.split(','):
        ticket.append(int(val))
    return ticket


# read the tickets
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

# throw out the bad ones
trash_bin = []
for ticket in nearby_tickets:
    for box in ticket:
        valid = False
        for value in ticket_data.values():
            if box in value:
                valid = True
                break
        if not valid:
            trash_bin.append(ticket)
            break

for trash in trash_bin:
    if trash in nearby_tickets:
        nearby_tickets.remove(trash)


# utility functioh
def is_field_possible(name, values):
    for val in values:
        if not val in ticket_data[name]:
            return False
    return True


# turn list of tickets into list of fields at position i
nearby_ticket_values = []

for i in range(len(nearby_tickets[0])):
    nearby_ticket_values.append([])
    for ticket in nearby_tickets:
        nearby_ticket_values[i].append(ticket[i])


# make a list of all possible keys on all possible locs
for i in range(len(ticket_data)):
    valid_ticket.append([])
    for key in ticket_data.keys():
        valid_ticket[i].append(key)


# kick out all fields that are impossible
for i in range(len(valid_ticket)):
    to_remove = []
    for field in valid_ticket[i]:
        if not is_field_possible(field, nearby_ticket_values[i]):
            to_remove.append(field)
    for trash in to_remove:
        valid_ticket[i].remove(trash)


def all_empty(ticket):
    return len([field for field in ticket if len(field) > 0]) == 0

field_positions = {}
# eliminate fields with exactly 1 entry (ok, so while testing I found that this is the last step, but there are possible steps after this)
while not all_empty(valid_ticket):
    field = [name for name in valid_ticket if len(name) == 1][0][0]
    position = valid_ticket.index([field])
    field_positions[field] = position
    for ticket in valid_ticket:
        if field in ticket:
            ticket.remove(field)

print(field_positions)

mult = 1
for key in field_positions.keys():
    if len(key) > 9 and key[0:9] == "departure":
        mult *= your_ticket[field_positions[key]]

print(mult)
