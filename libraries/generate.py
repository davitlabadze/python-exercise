import random
# only choice
# impoer random from choice
# coin = choice(["heads","tails"])

# choice
coin = random.choice(["heads","tails"])
print(coin)

# randint
num = random.randint(1,10)
print(num)


# shuffle

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

