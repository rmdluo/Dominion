"""
Situation: you start a game of dominion with 7 coppers and 3 estates in your
deck.
"""

from inventorVillageLaboratory import SingleGame

NUM_RUNS = 1000

turns = 0

for number in range(NUM_RUNS):
    #print(number)
    game = SingleGame()
    game.simulateRun()
    
    turns += game.turnNumber

print(turns / 1000)
