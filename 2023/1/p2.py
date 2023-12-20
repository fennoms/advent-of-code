numbers = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

total = 0
for line in open(0).read().splitlines():

    for key, value in numbers.items():
        line = line.replace(key, value)

    digits = [ch for ch in line if ch.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)