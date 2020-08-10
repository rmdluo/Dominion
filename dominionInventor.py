"""
Situation: you start a game of dominion with 7 coppers and 3 estates in your
deck.
"""

from inventorVillageLaboratoryOnly import SingleGame

NUM_RUNS = 1000

turns = 0

for number in range(NUM_RUNS):
    #print(number)
    game = SingleGame(10, 6, 6)
    game.simulateRun()
    
    turns += game.turnNumber

print(turns / 1000)
