num = open(0).read().strip()

for j in range(50):
    i = 0
    result = []
    while i < len(num):
        char = num[i]
        count = 1
        while i < len(num) - 1 and num[i + 1] == char:
            count += 1
            i += 1
        result.append(str(count) + char)
        i += 1

    num = "".join(result)
    result.clear()

print(len(num))
