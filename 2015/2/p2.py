t = 0

for line in open(0).read().splitlines():
    a = line.split("x")
    a = list(map(int, a))
    l, w, h = a

    t += l * w * h
    a.sort(reverse=True)
    t += 2 * a.pop() + 2 * a.pop()

print(t)
