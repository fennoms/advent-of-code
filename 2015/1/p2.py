d = open(0).read()
l = 0
for i, c in enumerate(d):
    if c == '(':
        l += 1
    else:
        l -= 1
    
    if l < 0:
        print(i + 1)
        break