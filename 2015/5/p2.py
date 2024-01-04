t = 0
for line in open(0).readlines():
    if not any(line[i] == line[i + 2] for i in range(len(line) - 2)):
        continue

    i = 0
    while i < len(line) - 1:
        pair = line[i] + line[i + 1]
        print(pair)

        if pair in line[i + 2 :]:
            break
        i += 1
    else:
        continue

    t += 1

print(t)
