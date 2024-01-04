grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in open(0).read().splitlines():
    num1 = int(line.split(",")[0].split()[-1])
    num2 = int(line.split(",")[1].split()[0])
    num3 = int(line.split(",")[1].split()[-1])
    num4 = int(line.split(",")[-1].split()[0])

    ranges = [(num1, num2), (num2, num3)]

    for i in range(num1, num3 + 1):
        for j in range(num2, num4 + 1):
            if "turn on" in line:
                grid[i][j] = 1

            if "turn off" in line:
                grid[i][j] = 0

            if "toggle" in line:
                grid[i][j] = 0 if grid[i][j] == 1 else 1

print(sum(sum(r) for r in grid))
