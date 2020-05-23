# Use the probability(hand, deck) function in this file 
# to calculate the probability of getting a certain hand 
# given a randomly shuffled deck.

# The main() function in this file
# computes the probability of getting all possible hands
# given a randomly shuffled deck containing 7 copper and 3 estate.

# Michael Chu
# 5/22/20

import math

HANDSIZE = 5

# Returns the number of spots left in the hand we're trying to build (given a certain base b)
def spotsLeft(b):
    spots = HANDSIZE
    for n in b.values():
        spots = spots - n
    return spots

# Calculates n choose r
def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

# Calculates the number of cards in deck d
def nCards(d):
    count = 0
    for n in d.values():
        count += n
    return count

# Returns all possible hands of 5 cards given a certain base and a certain deck
def hands(deck,base={}):
    # Makes copies so as to not disturb the originals
    d = deck.copy()
    b = base.copy()

    # If the deck is empty, return base (as long at it is a valid hand)
    if len(d)==0:
        spots = spotsLeft(b)
        if spots > 0:
            return []
        elif spots == 0:
            return [b]
        else:
            return ["INVALID HAND"]

    # Otherwise... Pick a card type from the deck 
    cardType = list(d)[0]
    amount = d[cardType]
    
    # Update the deck
    del d[cardType]

    # Figure out how many spots in the hand are left
    spots = spotsLeft(b)

    # Generate hands with i of the card type
    handList = []
    for i in range(0,min(spots,amount)+1):
        b[cardType] = i
        handList += hands(d,b)

    return handList

# Calculates probability of getting a certain hand given a randomly shuffled deck
def probability(hand,deck):
    successes = 1
    for card,amount in hand.items():    
        successes = successes*nCr(deck[card],amount)
    possible = nCr(nCards(deck),5)

    prob = successes/possible
    return prob

def main():
    deck = {"copper":7,
        "estate":3}
    print("Deck: ",deck)
    print()

    possibleHands = hands(deck)
    print("Possible Hands:")
    print(possibleHands)
    print()

    print("Probabilities:")
    probabilities = {}
    for hand in possibleHands:
        prob = probability(hand,deck)
        print(hand,prob)
        probabilities[tuple(hand.items())] = prob
    print()
    print(probabilities)
    print()

    sum = 0
    for prob in probabilities.values():
        sum += prob
    print("Sum of Probabilities: ",sum)

main()
