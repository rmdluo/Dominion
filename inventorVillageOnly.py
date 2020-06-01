"""
starts from the very beginning of the game

plays inventor village

if can get inventor or village, get whichever one there is less than

counts how many turns are needed to get all of the provinces

STARTS WITH 0 COPPERS AND 0 ESTATES ONLY VILLAGES AND INVENTORS

"""

import random

class SingleGame:
    def __init__(self, numInventors, numVillages):
        self.file = open("gameInventorVillageOnly.txt", "w")
        self.deck = []

        for card in range(numInventors):
            self.deck.append("action-inventor")

        for card in range(numVillages):
            self.deck.append("action-village")
        
        self.hand = []
        self.discard = []
        self.actions = 0
        self.buys = 0
        self.coins = 0
        self.turnNumber = 0
        self.provinces = 8
        self.numInventor = numInventors
        self.numVillage = numVillages
        self.costReduction = 0

    # simulates "inventor" game
    def simulateRun(self):
        self.shuffleDeck()
        self.draw(5)
        while(self.provinces > 0):
            self.turn()

        self.file.close()


    # simulates a turn
    def turn(self):

        self.costReduction = 0

        self.turnNumber += 1
        self.actions = 1
        self.buys = 1
        self.coins = 0

        self.file.write(str(self.turnNumber) + ": " + str(self.provinces) + ", " + str(self.numInventor) + ", " + str(self.numVillage) + "\n")
        self.file.write(str(self.hand) + "\n")

        self.action()

        self.file.write(str(self.hand) + "\n")
        
        self.buy()
        self.cleanUp()


    # 
    def action(self):
        playableActions = []

        # gets all of the actions in the hand
        for card in self.hand:
            if(card[:6] == "action"):
                playableActions.append(card)

        # plays the actions
        while(len(playableActions) > 0 and self.actions > 0):
            if("action-village" in playableActions):

                self.file.write("play village" + "\n")

                for number in range(1):
                    self.draw(1)
                    card = self.hand[len(self.hand) - 1]
                    if(card[:6] == "action"):
                        playableActions.append(card)
                
                self.actions += 2

                self.actions -= 1
                playableActions.remove("action-village")
             
            elif("action-inventor" in playableActions):

                self.file.write("play inventor" + "\n")
                
                if(8 - self.costReduction <= 4):
                    self.discard.append("victory-province")
                    self.provinces -= 1
                    
                elif(self.numInventor > self.numVillage): # if 10 villages have been bought then this cannot be true
                    self.discard.append("action-village")
                    self.numVillage += 1
                    
                elif(self.numInventor < self.numVillage): # if 10 inventors have been bought then this cannot be true
                    self.discard.append("action-inventor")
                    self.numInventor += 1

                else:
                    if(self.numInventor < 10):
                        self.discard.append("action-inventor")
                        self.numInventor += 1

                    elif(10 > self.numVillage): # if 10 villages have been bought then this cannot be true
                        self.discard.append("action-village")
                        self.numVillage += 1

                self.costReduction += 1
                self.actions -= 1
                playableActions.remove("action-inventor")

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

        while(self.buys > 0):
            if(8 - self.costReduction <= self.coins):
                self.discard.append("victory-province")
                self.coins -= 8
                self.provinces -= 1
                
            elif (4 - self.costReduction <= self.coins):
                if(self.numInventor < self.numVillage): # if 10 inventors have been bought then this cannot be true
                    self.discard.append("action-inventor")
                    self.numInventor += 1
                    self.coins -= 4
                    
                elif(self.numInventor > self.numVillage): # if 10 villages have been bought then this cannot be true
                    self.discard.append("action-village")
                    self.numVillage += 1
                    self.coins -= 3

                else:
                    if(self.numInventor < 10):
                        self.discard.append("action-inventor")
                        self.numInventor += 1
                        self.coins -= 4

                    elif(10 > self.numVillage): # if 10 villages have been bought then this cannot be true
                        self.discard.append("action-village")
                        self.numVillage += 1
                        self.coins -= 3
                    
            elif(3 - self.costReduction <= self.coins):
                if(self.numVillage < 10):
                    self.discard.append("action-village")
                    self.numVillage += 1
                    self.coins -= 3
                
            self.buys -= 1


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
            for card in self.deck:
                self.hand.append(card)
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
            
