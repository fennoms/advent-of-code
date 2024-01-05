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
        "points": 0,
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

    highest = []
    for horse in d.items():
        dist = horse[1]["distance"]

        if not highest or dist > highest[0][1]:
            highest = [(horse[0], dist)]

        elif dist == highest[0][1]:
            highest.append((horse[0], dist))

    for horse in highest:
        d[horse[0]]["points"] += 1


highest = 0
for horse in d.items():
    points = horse[1]["points"]

    if points > highest:
        highest = points

print(highest)
