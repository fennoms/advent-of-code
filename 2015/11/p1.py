pwd = open(0).read().strip()
pwd = list(pwd)

alph = "abcdefghijklmnopqrstuvwxyz"
pairs = [item + item for item in alph]
pairs2 = [alph[i] + alph[i + 1] + alph[i + 2] for i in range(len(alph) - 2)]


def increment(pwd):
    index = -1
    while index + len(pwd) >= 0:
        pwd[index] = ord(pwd[index]) + 1
        if pwd[index] == ord("z") + 1:
            pwd[index] = pwd[index] - 26
            pwd[index] = chr(pwd[index])
            index -= 1
        else:
            pwd[index] = chr(pwd[index])
            break

    return pwd


def valid(pwd):
    if "i" in pwd or "o" in pwd or "l" in pwd:
        return False

    if not any(pair in pwd for pair in pairs2):
        return False

    count = 0
    for pair in pairs:
        if pwd.find(pair) != -1:
            pwd = pwd.replace(pair, "0")
            count += 1

    if count < 2:
        return False

    return True


while not valid("".join(pwd)):
    pwd = increment(pwd)
    print(pwd)
print("".join(pwd))
