import hashlib

h = open(0).read().strip()
i = 0
while True:
    t = h + str(i)

    hs = hashlib.md5(t.encode())
    hs = hs.hexdigest()

    if "".join(hs[0:5]) == "00000":
        break
    i += 1

print(i)
