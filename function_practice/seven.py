def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    return 'BUST'

print(blackjack(5,6,27))