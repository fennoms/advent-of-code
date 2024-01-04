locations = {}
directions = {">": [1, 0], "<": [-1, 0], "^": [0, 1], "v": [0, -1]}

s = [0, 0]

for c in open(0).read():
    locations[tuple(s)] = 1

    n = directions[c]

    s[0] += n[0]
    s[1] += n[1]

print(sum(locations.values()))
