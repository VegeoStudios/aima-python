loc_A, loc_B, loc_C, loc_D = (0, 0), (1, 0), (0, 1), (1, 1)
locations = [loc_A, loc_B, loc_C, loc_D]
table = {}

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for loc in range(4):
                    state = (a, b, c, d)
                    percept = []
                    # Start program
                    for i in range (4):
                        if state[loc] == 1:
                            percept.append((locations[loc], 'Dirty'))
                            table[tuple(percept)] = 'Suck'
                        percept.append((locations[loc], 'Clean'))
                        if loc == 0:
                            table[tuple(percept)] = 'Right'
                            loc = 1
                        elif loc == 1:
                            table[tuple(percept)] = 'Down'
                            loc = 3
                        elif loc == 3:
                            table[tuple(percept)] = 'Left'
                            loc = 2
                        elif loc == 2:
                            table[tuple(percept)] = 'Up'
                            loc = 0
print(table.__len__())