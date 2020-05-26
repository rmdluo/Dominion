"""
This is the class to simulate a game where you try to get a moneylender and
silver in the first two turns.
"""

import random

class SingleGame:
    def __init__(self):
        self.deck = ["treasure-copper", "treasure-copper", "treasure-copper", "treasure-copper", "treasure-copper", "treasure-copper", "treasure-copper", "treasure-silver", "victory-estate", "victory-estate", "victory-estate", "action-moneylender"]
        self.hand = []
        self.discard = []
        self.actions = 0
        self.buys = 0
        self.coins = 0
        self.turnNumber = 0

        # coinages on turns 1, 2, 3, and 4
        self.a = 0
        self.b = 0
        #self.c = 0
        #self.d = 0


    # simulates a "moneylender" game up to 4 turns
    def simulateRun(self):
        self.shuffleDeck()
        self.draw(5)
        for number in range(2):
            self.turn()


    # simulates a turn
    def turn(self):
        self.turnNumber += 1
        self.actions = 1
        self.buys = 1
        self.coins = 0
        
        self.action()
        self.buy()
        self.cleanUp()


    # considering that the only action we will care about in this case is
    # the moneylender, we will only implement moneylender here, but more
    # implementations can be added for different action cards
    def action(self):
        playableActions = []

        # gets all of the actions in the hand
        for card in self.hand:
            if(card[:6] == "action"):
                playableActions.append(card)

        # plays the actions
        while(len(playableActions) > 0 and self.actions > 0):
            if("action-moneylender" in playableActions):

                # moneylender trashes 1 copper to gain 3 coins
                if("treasure-copper" in self.hand):
                    self.hand.remove("treasure-copper")
                    self.coins += 3

                self.actions -= 1
                playableActions.remove("action-moneylender")


    # buys stuff based on criteria we decided
    def buy(self):
        # plays all of the treasures that can be played
        for card in self.hand:
            if(card[:8] == "treasure"):
                if(card[9:] == "copper"):
                    self.coins += 1
                elif (card[9:] == "silver"):
                    self.coins += 2
                else:
                    self.coins += 3

        # stores coinage on a particular turn
        if(self.turnNumber == 1):
            self.a = self.coins
        elif (self.turnNumber == 2):
            self.b = self.coins
        #elif(self.turnNumber == 3):
        #    self.c = self.coins
        #elif (self.turnNumber == 4):
        #    self.d = self.coins

        # makes buying decision
        # buy a gold if enough money
        # buy a moneylender if enough money
        # buy a silver if enough money
        if(self.coins >= 6):
            self.discard.append("treasure-gold")
            self.coins -= 6
        elif(self.coins >= 4):
            self.discard.append("action-moneylender")
            self.coins -= 4
        elif (self.coins >= 3):
            self.discard.append("treasure-silver")
            self.coins -= 3


    # gets rid of cards and ends the turn
    def cleanUp(self):
        # since none of the cards are taken out of the hand prior to this,
        # we discard everything during the clean-up phase
        for card in self.hand:
            self.discard.append(card)

        # we empty the hand and draw 5 new cards
        self.hand = []
        self.draw(5)

    
    # draws a specified number of cards to the hand
    def draw(self, numCardsWanted):
        # how many cards have been drawn
        numDrawn = 0

        # run this if there are not enough cards in the deck
        if(len(self.deck) < numCardsWanted):
            # put the cards in the deck right now in the hand
            self.hand = self.deck.copy()
            numDrawn += len(self.hand)

            # shuffle the discard pile and make it the new deck
            self.deck = self.discard.copy()
            self.discard = []
            self.shuffleDeck()

        # add cards from the deck until the right number of cards have been drawn
        while(numDrawn < numCardsWanted):
            try:
                self.hand.append(self.deck.pop(0))
            except IndexError:
                pass
            numDrawn += 1

    def shuffleDeck(self):
        # just shuffles the deck
        random.shuffle(self.deck)
            
