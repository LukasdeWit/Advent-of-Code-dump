buses = []

file = open("day 13 puzzle 1 data.txt")
useless_nonsense_variable_that_doesnt_get_used = file.readline()
index = 0
for bus in file.readline().split(','):
    if not bus == 'x':
        buses.append(((-index) % int(bus), int(bus)))
    index += 1


''' #dreaded be he, who dares run this code, for it is long and winding
t = 100000000000000
length = len(buses)
looping = True
while looping:
    corr = 0
    for bus_i in range(len(buses)):
        if (t + bus_i) % buses[bus_i] == 0:
            corr += 1
        else:
            break
    if corr == length:
        looping = False
    else:
        t += 1
print(t)
'''

# hint: https://nl.wikipedia.org/wiki/Chinese_reststelling
# tweede hint: https://docplayer.nl/6329174-De-chinese-reststelling.html
# buses is nu een stelsel van modulos die we oplossen met de chinese reststelling
# de eerste stap: maak alle getallen copriem, is niet nodig want alle getallen
# zijn priem dus per definitie ook copriem (want alle getallen zijn ongelijk haha pak aan myrte dit is correct)

# bereken alle getallen met elkaar vermenigvuldigt om te weten wat de stapgrootte
# voor repetitie is
mult = 1
for bus in buses:
    mult *= bus[1]
# voor iedere bus, bereken het versimpelde stelsel uit
vals = []
for bus in buses:
    vals.append(pow(mult // bus[1], -1, bus[1]) * mult // bus[1])

for i in range(len(buses)):
    vals[i] = vals[i] * buses[i][0]

print(sum(vals)%(mult))
# alle antwoorden x op de vraag zijn nu mods + mult * k, waar k is in N
# we willen de eerste, dus k == 0, dus x = mods



''' # '''
