total = 0
for i, line in enumerate(open(0)):
    games = line.strip().split(': ')[1].split(';')

    d = {"red": 0, "green": 0, "blue": 0}
    for game in games:

        for ball in game.split(','):
            amount, color = ball.split()
            d[color] = max(int(amount), d[color])

    if not (d["blue"] > 14 or d["red"] > 12 or d["green"] > 13):
        total += (i + 1)

print(total)