rolls = []
game_string = 'X7/9-X-88/-6XXX81'

for c in game_string:
    if c == 'X':
        rolls.append(10)
    elif c == '-':
        rolls.append(0)
    elif c == '/':
        previous = rolls[-1]
        rolls.append(10 - previous)
    else:
        rolls.append(int(c))
print(rolls)

