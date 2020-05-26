"""
Situation: you start a game of dominion with 7 coppers and 3 estates in your
deck. In the first 2 turns, you buy silver and moneylender if you can. On turns
3 and 4, you want to figure out what the possible coinages are. Note that this
does not assume that you successfully bought a silver or moneylender in the
first two turns.
"""

from MoneyLender import SingleGame

NUM_RUNS = 100000

# possible coinages on turns 1, 2, 3, and 4
# [1 coin, 2 coins, 3 coins, 4 coins, 5 coins, 6 coins, 7 coins]
outcomesA = [0, 0, 0, 0, 0, 0, 0]
outcomesB = [0, 0, 0, 0, 0, 0, 0]
#outcomesC = [0, 0, 0, 0, 0, 0, 0]
#outcomesD = [0, 0, 0, 0, 0, 0, 0]

print("Moneylender + silver simulated " + str(NUM_RUNS) + " times:")

for number in range(NUM_RUNS):
    game = SingleGame()
    game.simulateRun()

    # update possible coinages
    outcomesA[game.a - 1] += 1
    outcomesB[game.b - 1] += 1
    #outcomesC[game.c - 1] += 1
    #outcomesD[game.d - 1] += 1

print("Possible coinage on turn 1: " + str(outcomesA))
print("Possible coinage on turn 2: " + str(outcomesB))
#print("Possible coinage on turn 3: " + str(outcomesC))
#print("Possible coinage on turn 4: " + str(outcomesD))
