locations = {}
directions = {">": [1, 0], "<": [-1, 0], "^": [0, 1], "v": [0, -1]}

s = [0, 0]
r = [0, 0]
d = open(0).read()

for i in range(0, len(d), 2):
    c = d[i]
    c2 = d[i + 1]

    n = directions[c]
    n2 = directions[c2]

    s[0] += n[0]
    s[1] += n[1]

    r[0] += n2[0]
    r[1] += n2[1]

    locations[tuple(s)] = 1
    locations[tuple(r)] = 1

print(sum(locations.values()))
