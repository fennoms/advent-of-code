vowels = "aeiou"
n = ["ab", "cd", "pq", "xy"]
doubles = [item + item for item in "abcdefghijklmnopqrstuvwxyz"]

t = 0
for line in open(0).readlines():
    if sum([line.count(x) for x in vowels]) < 3:
        continue

    if not any(double in line for double in doubles):
        continue

    if any(n in line for n in n):
        continue

    t += 1

print(t)
