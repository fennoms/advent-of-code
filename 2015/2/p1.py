t = 0

for line in open(0).read().splitlines():
    l, w, h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    t += ((2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, l * h, w * h))

print(t)