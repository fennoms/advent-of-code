s = 2503
d = {}
for line in open(0).read().splitlines():
    a, *b = line.split()
    a = a.strip()
    speed = int(b[2])
    time = int(b[5])
    rest = int(b[-2])
    d[a] = {
        "speed": speed,
        "time": time,
        "rest": rest,
        "cur_mov": 0,
        "cur_rest": 0,
        "distance": 0,
        "resting": False,
    }


for i in range(s):
    for horse in d.keys():
        horse = d[horse]

        if not horse["resting"]:
            horse["distance"] += horse["speed"]

            horse["cur_mov"] += 1
            if horse["cur_mov"] == horse["time"]:
                horse["resting"] = True
                horse["cur_mov"] = 0
        else:
            horse["cur_rest"] += 1
            if horse["cur_rest"] == horse["rest"]:
                horse["resting"] = False
                horse["cur_rest"] = 0


highest = 0
for horse in d.items():
    dist = horse[1]["distance"]
    if dist > highest:
        highest = dist

print(highest)
