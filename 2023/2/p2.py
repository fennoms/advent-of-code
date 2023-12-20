total = 0
for line in open(0):
    games = line.strip().split(': ')[1].split(';')

    d = {"red": 0, "green": 0, "blue": 0}
    for game in games:

        for ball in game.split(','):
            amount, color = ball.split()
            d[color] = max(int(amount), d[color])

    total += (d["red"] * d["blue"] * d["green"])

print(total)