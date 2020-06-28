import math

HANDSIZE = 5

# Returns the number of spots left in the draw of n cards we're trying to build (given a certain base b)
def spotsLeft(b,n=HANDSIZE):
    spots = n
    for i in b.values():
        spots = spots - i
    return spots

# Calculates n choose r
def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

# Calculates the number of cards in dictionary d
def nCards(d):
    count = 0
    for n in d.values():
        count += n
    return count

# Returns all possible draws of n cards given a certain base and a certain deck
# Returns a list of dictionary draws
def possDraws(deck,base={},n=5):
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

    # Figure out how many spots in the draw are left
    spots = spotsLeft(b,n)

    # Generate draws with i of the card type
    drawList = []
    for i in range(0,min(spots,amount)+1):
        b[cardType] = i
        drawList += possDraws(d,b)

    return drawList
    
# Calculates probability of getting a certain draw given a randomly shuffled deck
def probDraw(draw,deck):
    successes = 1
    for card,amount in draw.items():    
        successes = successes*nCr(deck[card],amount)
    possible = nCr(nCards(deck),nCards(draw))

    prob = successes/possible
    return prob

# Prints starting probabilities for deck of 7 copper and 3 estate
# Useful for demonstration purposes because it prints out lots of stuff
def startingProbabilities():
    deck = {"copper":7,
        "estate":3}
    print("Deck: ",deck)
    print()

    possibleHands = possDraws(deck)
    print("Possible Hands:")
    print(possibleHands)
    print()

    print("Probabilities:")
    probabilities = {}
    for hand in possibleHands:
        prob = possDraws(hand,deck)
        print(hand,prob)
        probabilities[tuple(hand.items())] = prob
    print()
    print(probabilities)
    print()

    sum = 0
    for prob in probabilities.values():
        sum += prob
    print("Sum of Probabilities: ",sum)

# Note: this method spends money without getting rid of the copper, silver, and gold cards
def actions(deck,hand,turnNumber):
    cardTypes = hand.keys()
    money = calcMoney(hand)
    while "moneylender" in cardTypes:
        money = playMoneylender(hand,money)
    while money >= 4:
        money = buyMoneylender(hand,money)
    while money >= 3:
        money = buySilver(hand,money)

def buySilver(hand,money):
    if money < 3:
        return "NOT ENOUGH MONEY TO BUY A SILVER"
    else:
        money -= 3
        if "silver" in cardTypes:
            hand["silver"] += 1
        else:
            hand["silver"] = 1
        return money

def calcMoney(hand):
    cardTypes = hand.keys()
    total = 0
    for moneyCard in ["copper","silver","gold"]:
        if moneyCard in cardTypes:
            total += hand[moneyCard]*value(moneyCard)
    return total

def value(moneyCard):
    if moneyCard=="copper":
        return 1
    if moneyCard=="silver":
        return 2
    if moneyCard=="gold":
        return 3

def buyMoneylender(hand,money):
    cardTypes = hand.keys()
    if money < 4:
        return "NOT ENOUGH MONEY TO BUY MONEYLENDER!"
    else:
        money -= 4
        if "moneylender" in cardTypes:
            hand["moneylender"] += 1
        else:
            hand["moneylender"] = 1
        return money

def playMoneylender(hand,money):
    cardTypes = hand.keys()
    if "moneylender" not in cardTypes:
        return "NO MONEYLENDER IN HAND!"
    elif "copper" not in cardTypes:
        return "NO COPPER IN HAND!"
    else:
        hand["moneylender"] -= 1
        money += 3
        return money


def turn(deck,handHistProb,):    
    # Generate possible hands and probabilities
    possibleHands = possDraws(deck)
    probabilities = {}
    for hand in possibleHands:
        prob = probDraw(hand,deck)
        probabilities[tuple(hand.items())] = prob

    # Loop through each possible hand
    for hand in possibleHands:
        [deck,hand] = actions(deck, hand, 1)

def simulateFourTurns():
    # Starting deck
    deck = {"copper":7,
        "estate":3}
