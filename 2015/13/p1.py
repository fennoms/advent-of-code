import itertools

h = {}
names = set()
for line in open(0).read().splitlines():
    num = int("".join([x for x in line if x.isdigit()]))

    if "lose" in line:
        num *= -1

    a = line.split()[0].strip()
    b = line.split()[-1][0:-1]

    if not h.get(a):
        h[a] = {}
    h[a][b] = num

    names.add(a)
    names.add(b)

best = 0
for perm in itertools.permutations(names):
    i = 0
    total = 0
    while True:
        p1 = perm[i]
        p2 = perm[(i + 1) % len(perm)]
        p3 = perm[(i - 1 + len(perm)) if i - 1 < 0 else i - 1]

        total += (h[p1][p2]) + (h[p1][p3])

        if (i + 1) % len(perm) == 0:
            break
        i += 1

    if total > best:
        best = total

print(best)
